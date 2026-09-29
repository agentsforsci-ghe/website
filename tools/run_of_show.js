/* Run of show app. Inlined into workshop/run-of-show.html by
   tools/build_run_of_show.py. The pure part (ROS.*) is also loadable by
   Node for tests: node --test tools/run_of_show.test.js */
(function () {
  'use strict';

  var ROS = {};

  /* ---------- pure helpers ---------- */

  ROS.minutesOf = function (hhmm) {
    var p = hhmm.split(':');
    return Number(p[0]) * 60 + Number(p[1]);
  };

  ROS.pad = function (n) { return (n < 10 ? '0' : '') + n; };

  // Seconds -> "m:ss" under an hour, "h:mm:ss" above. Negative -> "-m:ss".
  ROS.fmtDur = function (secs) {
    var neg = secs < 0;
    var s = Math.abs(Math.round(secs));
    var h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), r = s % 60;
    var out = h > 0 ? h + ':' + ROS.pad(m) + ':' + ROS.pad(r) : m + ':' + ROS.pad(r);
    return (neg ? '-' : '') + out;
  };

  ROS.fmtMin = function (mins) {
    var m = Math.abs(mins);
    return m + ' min';
  };

  // Local clock time "HH:MM" of an epoch ms in the given IANA zone.
  ROS.clockIn = function (ms, tz, withSeconds) {
    try {
      var f = new Intl.DateTimeFormat('en-GB', { timeZone: tz, hour: '2-digit', minute: '2-digit', second: withSeconds ? '2-digit' : undefined, hour12: false });
      return f.format(new Date(ms));
    } catch (e) {
      var d = new Date(ms);
      return ROS.pad(d.getHours()) + ':' + ROS.pad(d.getMinutes()) + (withSeconds ? ':' + ROS.pad(d.getSeconds()) : '');
    }
  };

  ROS.dateIn = function (ms, tz) {
    try {
      var f = new Intl.DateTimeFormat('en-CA', { timeZone: tz, year: 'numeric', month: '2-digit', day: '2-digit' });
      return f.format(new Date(ms));
    } catch (e) {
      var d = new Date(ms);
      return d.getFullYear() + '-' + ROS.pad(d.getMonth() + 1) + '-' + ROS.pad(d.getDate());
    }
  };

  ROS.blankState = function (runDate, device) {
    return { schema: 1, runDate: runDate, updatedAt: null, device: device || null, blocks: {}, ticks: {} };
  };

  /* derive(data, state, nowMs): every number the screen shows.
     live: the run date is the workshop date, so drift compares with the
     printed clock times. Otherwise (a rehearsal) drift compares with the
     planned durations measured from the first Start tap. */
  ROS.derive = function (data, state, nowMs) {
    var live = state.runDate === data.workshopDate;
    var blocks = data.blocks;
    var out = { live: live, blocks: {}, runningId: null, nextId: null, firstStartedAt: null };
    var t0 = null, first = null;
    var i, b, s, t;
    for (i = 0; i < blocks.length; i++) {
      b = blocks[i]; s = state.blocks[b.id];
      if (s && s.startedAt) {
        t = Date.parse(s.startedAt);
        if (t0 === null || t < t0) { t0 = t; first = b; }
      }
    }
    out.firstStartedAt = t0;
    for (i = 0; i < blocks.length; i++) {
      b = blocks[i]; s = state.blocks[b.id] || {};
      var startedAt = s.startedAt ? Date.parse(s.startedAt) : null;
      var endedAt = s.endedAt ? Date.parse(s.endedAt) : null;
      var status = 'later';
      if (startedAt && !endedAt) status = 'running';
      else if (startedAt && endedAt) status = 'done';
      var plannedSec = b.min * 60;
      var d = { status: status, running: null, left: null, over: false, startDrift: null, endDrift: null,
                projectedEnd: null, startedAt: startedAt, endedAt: endedAt, actualMin: null };
      if (startedAt) {
        d.running = Math.floor(((endedAt || nowMs) - startedAt) / 1000);
        d.left = plannedSec - d.running;
        d.over = d.left < 0;
        d.projectedEnd = endedAt || Math.max(nowMs, startedAt + plannedSec * 1000);
        if (endedAt) d.actualMin = Math.round((endedAt - startedAt) / 60000);
        if (live) {
          d.startDrift = Math.round((startedAt - Date.parse(b.startIso)) / 60000);
          d.endDrift = Math.round((d.projectedEnd - Date.parse(b.endIso)) / 60000);
        } else if (t0 !== null) {
          var offset = (ROS.minutesOf(b.start) - ROS.minutesOf(first.start)) * 60000;
          d.startDrift = Math.round(((startedAt - t0) - offset) / 60000);
          d.endDrift = Math.round(((d.projectedEnd - t0) - (offset + plannedSec * 1000)) / 60000);
        }
      }
      if (status === 'running') out.runningId = b.id;
      out.blocks[b.id] = d;
    }
    // next: the first block after the running one (or after the last done one) that has not started
    var anchor = -1;
    for (i = 0; i < blocks.length; i++) {
      if (out.blocks[blocks[i].id].status !== 'later') anchor = i;
    }
    for (i = anchor + 1; i < blocks.length; i++) {
      if (out.blocks[blocks[i].id].status === 'later') { out.nextId = blocks[i].id; break; }
    }
    if (out.nextId === null) {
      for (i = 0; i < blocks.length; i++) {
        if (out.blocks[blocks[i].id].status === 'later') { out.nextId = blocks[i].id; break; }
      }
    }
    return out;
  };

  /* state transitions; each returns the (mutated) state with updatedAt set */
  function stamp(state, nowIso) { state.updatedAt = nowIso; return state; }

  ROS.start = function (state, id, nowIso) {
    var k;
    for (k in state.blocks) {
      if (k !== id && state.blocks[k].startedAt && !state.blocks[k].endedAt) state.blocks[k].endedAt = nowIso;
    }
    state.blocks[id] = { startedAt: nowIso, endedAt: null };
    return stamp(state, nowIso);
  };
  ROS.end = function (state, id, nowIso) {
    var s = state.blocks[id];
    if (s && s.startedAt && !s.endedAt) s.endedAt = nowIso;
    return stamp(state, nowIso);
  };
  ROS.restart = function (state, id, nowIso) {
    return ROS.start(state, id, nowIso);
  };
  ROS.toggle = function (state, itemId, nowIso) {
    if (state.ticks[itemId]) delete state.ticks[itemId]; else state.ticks[itemId] = nowIso;
    return stamp(state, nowIso);
  };
  ROS.reset = function (state, nowIso) {
    state.blocks = {}; state.ticks = {};
    return stamp(state, nowIso);
  };

  ROS.exportLog = function (data, state, nowMs) {
    var d = ROS.derive(data, state, nowMs);
    var labels = {};
    data.blocks.forEach(function (b) {
      b.rows.forEach(function (r) { labels[r.id] = { block: b.id, label: r.label, min: r.min }; });
      b.sections.forEach(function (s) {
        s.content.forEach(function (node) {
          if (node.t === 'ol') node.items.forEach(function (it) { if (it.id) labels[it.id] = { block: b.id, label: it.text, min: it.min }; });
        });
      });
    });
    (data.lists.before || []).forEach(function (it) { labels[it.id] = { block: 'before', label: it.text, min: null }; });
    (data.lists.arrival || []).forEach(function (it) { labels[it.id] = { block: 'arrival', label: it.text, min: null }; });
    (data.lists.after || []).forEach(function (it) { labels[it.id] = { block: 'after', label: it.text, min: null }; });
    var blocks = data.blocks.map(function (b) {
      var x = d.blocks[b.id];
      return { id: b.id, title: b.title, plannedStart: b.start, plannedEnd: b.end, plannedMin: b.min,
               startedAt: x.startedAt ? new Date(x.startedAt).toISOString() : null,
               endedAt: x.endedAt ? new Date(x.endedAt).toISOString() : null,
               actualMin: x.actualMin, startDriftMin: x.startDrift, endDriftMin: x.endDrift };
    });
    var ticks = Object.keys(state.ticks).sort(function (a, b) { return state.ticks[a] < state.ticks[b] ? -1 : 1; }).map(function (id) {
      var l = labels[id] || { block: null, label: id, min: null };
      var bx = l.block && d.blocks[l.block];
      var minInto = (bx && bx.startedAt) ? Math.round((Date.parse(state.ticks[id]) - bx.startedAt) / 60000) : null;
      return { id: id, block: l.block, label: l.label, plannedMin: l.min, doneAt: state.ticks[id], minIntoBlock: minInto };
    });
    return { date: state.runDate, live: d.live, exportedAt: new Date(nowMs).toISOString(), blocks: blocks, ticks: ticks };
  };

  if (typeof module !== 'undefined' && module.exports) module.exports = ROS;
  if (typeof document === 'undefined') return;

  /* ---------- the app ---------- */

  var data = JSON.parse(document.getElementById('ros-data').textContent);
  var TZ = data.timeZone || 'Europe/Zurich';
  var runDate = ROS.dateIn(Date.now(), TZ);
  var KEY = 'ros:' + runDate;
  var UIKEY = 'ros:ui';
  var device = null;
  var state = null;
  var ui = { tab: 'day', block: null, open: {}, wanted: false };
  var dbRef = null, writing = false, dirty = false;
  var wakeLock = null;
  var armed = {};

  var byId = {};
  data.blocks.forEach(function (b) { byId[b.id] = b; });

  function $(sel, root) { return (root || document).querySelector(sel); }
  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text !== undefined && text !== null) e.textContent = text;
    return e;
  }
  function nowIso() { return new Date().toISOString(); }

  /* storage */
  function lsGet(k) { try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : null; } catch (e) { return null; } }
  function lsSet(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); return true; } catch (e) { return false; } }

  function loadState() {
    var s = lsGet(KEY);
    if (!s || s.schema !== 1) s = ROS.blankState(runDate, device);
    return s;
  }
  function saveUi() { lsSet(UIKEY, { tab: ui.tab, block: ui.block, open: ui.open }); }
  function loadUi() {
    var u = lsGet(UIKEY);
    if (u) { ui.tab = u.tab || 'day'; ui.block = u.block || null; ui.open = u.open || {}; }
  }

  function commit() {
    state.device = device;
    if (!lsSet(KEY, state)) setBanner('This browser is not keeping the ticks between reloads (storage is blocked). They stay on screen for this visit only.');
    pushDb();
    renderAll();
  }

  function pushDb() {
    if (!dbRef) return;
    if (writing) { dirty = true; return; }
    writing = true;
    dbRef.set(state).then(function () {
      writing = false; setSync('synced');
      if (dirty) { dirty = false; pushDb(); }
    }, function () {
      writing = false; setSync('local');
    });
  }

  function adopt(remote) {
    state = JSON.parse(JSON.stringify(remote));
    lsSet(KEY, state);
    renderAll();
  }

  function connectDb() {
    var c = window.claude;
    if (!c || typeof c.use !== 'function') return;
    var p;
    try { p = c.use('db'); } catch (e) { return; }
    if (!p || typeof p.then !== 'function') return;
    p.then(function (db) {
      if (!db) return;
      var ref;
      try { ref = db.doc('runs/' + runDate); } catch (e) { return; }
      ref.get().then(function (snap) {
        var remote = snap.exists ? snap.data() : null;
        if (remote && remote.schema === 1 && (!state.updatedAt || (remote.updatedAt && remote.updatedAt > state.updatedAt))) {
          adopt(remote);
        } else if (state.updatedAt) {
          ref.set(state).catch(function () {});
        }
        dbRef = ref;
        setSync('synced');
        ref.onSnapshot(function (s2) {
          if (!s2.exists || s2.metadata.hasPendingWrites) return;
          var r = s2.data();
          if (r && r.schema === 1 && r.updatedAt && (!state.updatedAt || r.updatedAt > state.updatedAt)) adopt(r);
        }, function () { setSync('local'); });
      }, function () { setSync('local'); });
    }, function () {});
  }

  /* wake lock */
  function wake() {
    if (!ui.wanted || !('wakeLock' in navigator)) return;
    try {
      navigator.wakeLock.request('screen').then(function (l) {
        wakeLock = l; setWake(true);
        l.addEventListener('release', function () { wakeLock = null; setWake(false); });
      }, function () { setWake(false); });
    } catch (e) { setWake(false); }
  }

  /* header state pills */
  function setWake(on) { var e = $('#wake'); if (e) { e.textContent = on ? 'screen awake' : 'screen may sleep'; e.classList.toggle('on', on); } }
  function setSync(mode) { var e = $('#sync'); if (e) { e.textContent = mode === 'synced' ? 'synced' : 'this device'; e.classList.toggle('on', mode === 'synced'); } }
  function setBanner(text) { var e = $('#banner'); if (!e) return; e.textContent = text || ''; e.hidden = !text; }

  /* in-page confirm: first tap arms the button for five seconds */
  function confirmTap(btn, key, label, fn) {
    if (armed[key]) {
      clearTimeout(armed[key]); delete armed[key];
      btn.classList.remove('armed'); btn.textContent = label;
      fn();
      return;
    }
    btn.classList.add('armed'); btn.textContent = 'Tap again to ' + label.toLowerCase();
    armed[key] = setTimeout(function () { delete armed[key]; btn.classList.remove('armed'); btn.textContent = label; }, 5000);
  }

  /* ---------- rendering ---------- */

  function driftWord(n, late, early) {
    if (n === 0) return 'on plan';
    return n > 0 ? n + ' min ' + late : (-n) + ' min ' + early;
  }

  // "started 3 min late, ends 12:03, 3 min behind (planned 12:00)"
  function fmtDriftLine(b, d) {
    if (d.startDrift === null) return '';
    var parts = ['started ' + driftWord(d.startDrift, 'late', 'early')];
    if (d.endDrift !== null) {
      var endTxt = d.endedAt ? 'ended' : 'ends';
      var when = d.live ? ' ' + ROS.clockIn(d.projectedEnd, TZ) + ',' : '';
      parts.push(endTxt + when + ' ' + driftWord(d.endDrift, 'behind', 'ahead') + (d.live ? ' (planned ' + b.end + ')' : ''));
    }
    return parts.join(', ');
  }

  function renderHeader() {
    var now = Date.now();
    var d = ROS.derive(data, state, now);
    var hdr = $('#hdr');
    $('#clockTime').textContent = ROS.clockIn(now, TZ, true);
    $('#clockDate').textContent = d.live ? 'workshop day' : 'rehearsal, ' + runDate;
    var title = $('#hdrTitle'), run = $('#running'), left = $('#left'), drift = $('#drift');
    var rb = d.runningId ? byId[d.runningId] : null;
    if (rb) {
      var x = d.blocks[rb.id];
      title.textContent = rb.title;
      run.textContent = ROS.fmtDur(x.running);
      left.textContent = x.over ? 'over ' + ROS.fmtDur(-x.left) : ROS.fmtDur(x.left);
      left.classList.toggle('over', x.over);
      left.classList.toggle('soon', !x.over && x.left <= 120);
      hdr.classList.toggle('over', x.over);
      drift.textContent = fmtDriftLine(rb, { startDrift: x.startDrift, endDrift: x.endDrift, endedAt: x.endedAt, projectedEnd: x.projectedEnd, live: d.live, end: rb.end });
      drift.classList.toggle('behind', x.endDrift !== null && x.endDrift > 0);
    } else {
      var nb = d.nextId ? byId[d.nextId] : null;
      title.textContent = nb ? 'Next: ' + nb.title : 'Day complete';
      run.textContent = '--:--';
      left.textContent = nb ? nb.min + ' min' : '--:--';
      left.classList.remove('over'); left.classList.remove('soon'); hdr.classList.remove('over');
      if (nb && d.live) {
        var until = Math.round((Date.parse(nb.startIso) - now) / 60000);
        drift.textContent = until >= 0 ? 'planned ' + nb.start + ', in ' + until + ' min' : 'planned ' + nb.start + ', ' + (-until) + ' min ago';
        drift.classList.toggle('behind', until < 0);
      } else if (nb) {
        drift.textContent = 'planned ' + nb.start + ' to ' + nb.end;
        drift.classList.remove('behind');
      } else {
        drift.textContent = '';
        drift.classList.remove('behind');
      }
    }
  }

  function tagPills(tags, cls) {
    var frag = document.createDocumentFragment();
    (tags || []).forEach(function (t) { frag.appendChild(el('span', cls + (/PROTECTED|HARD START/.test(t) ? ' warn' : ''), t.toLowerCase())); });
    return frag;
  }

  function renderBlocks(d) {
    var box = $('#blocks');
    box.innerHTML = '';
    data.blocks.forEach(function (b) {
      var x = d.blocks[b.id];
      var btn = el('button', 'blk ' + x.status + (b.id === d.nextId ? ' next' : '') + (b.id === ui.block ? ' open' : ''));
      btn.setAttribute('type', 'button');
      btn.appendChild(el('span', 'when num', b.start + ' to ' + b.end));
      var t = el('span', 't', b.title);
      (b.tags || []).forEach(function (tg) { if (/PROTECTED|HARD START/.test(tg)) t.appendChild(el('span', 'tag', tg.toLowerCase())); });
      btn.appendChild(t);
      var sub = '';
      if (x.status === 'running') sub = 'running, ' + ROS.fmtDur(x.running) + (x.over ? ' (over)' : ' of ' + b.min + ' min');
      else if (x.status === 'done') sub = 'done, ' + ROS.clockIn(x.startedAt, TZ) + ' to ' + ROS.clockIn(x.endedAt, TZ) + ' (' + x.actualMin + ' of ' + b.min + ' min)';
      else sub = b.min + ' min' + (b.id === d.nextId ? ', next' : '');
      btn.appendChild(el('span', 'sub num', sub));
      btn.addEventListener('click', function () { ui.block = b.id; document.body.classList.remove('show-list'); saveUi(); renderAll(); });
      box.appendChild(btn);
    });
  }

  function inlineHtml(html) { var s = el('span'); s.innerHTML = html; return s; }

  function renderSection(sec, blockId) {
    var wrap = el('div', 'sec');
    var h = el('h3');
    h.appendChild(document.createTextNode(sec.title + ' '));
    if (sec.min) h.appendChild(el('span', 'pill', sec.min + ' min' + (sec.countdown && sec.countdown !== sec.min ? ', countdown ' + sec.countdown : '')));
    h.appendChild(tagPills(sec.tags, 'pill'));
    wrap.appendChild(h);
    sec.content.forEach(function (node) { wrap.appendChild(renderNode(node, blockId)); });
    return wrap;
  }

  function renderNode(node, blockId) {
    if (node.t === 'p') { var p = el('p'); p.innerHTML = node.html; return p; }
    if (node.t === 'ul') {
      var ul = el('ul');
      node.items.forEach(function (it) {
        var li = el('li'); li.appendChild(inlineHtml(it.html));
        (it.children || []).forEach(function (c) { li.appendChild(renderNode(c, blockId)); });
        ul.appendChild(li);
      });
      return ul;
    }
    if (node.t === 'ol') {
      var tickable = node.items.some(function (it) { return it.id; });
      var ol = el('ol', tickable ? 'steps' : '');
      node.items.forEach(function (it) {
        var li = el('li');
        if (it.id) {
          var done = !!state.ticks[it.id];
          if (done) li.classList.add('done');
          var tb = el('button', 'tick', '✓');
          tb.setAttribute('type', 'button'); tb.setAttribute('aria-pressed', done ? 'true' : 'false'); tb.setAttribute('aria-label', 'done');
          tb.addEventListener('click', function () { ROS.toggle(state, it.id, nowIso()); commit(); });
          li.appendChild(tb);
          li.appendChild(el('span', 'n num', it.n + '.'));
          var txt = el('span', 'txt'); txt.innerHTML = it.html; li.appendChild(txt);
          li.appendChild(el('span', 'smin num', it.min ? it.min + ' min' : ''));
        } else {
          li.appendChild(inlineHtml(it.html));
        }
        (it.children || []).forEach(function (c) { li.appendChild(renderNode(c, blockId)); });
        ol.appendChild(li);
      });
      return ol;
    }
    return el('div');
  }

  function renderPanel(d) {
    var panel = $('#panel');
    panel.innerHTML = '';
    var b = byId[ui.block] || byId[d.runningId] || byId[d.nextId] || data.blocks[0];
    if (!b) return;
    ui.block = b.id;
    var x = d.blocks[b.id];
    var secById = {};
    b.sections.forEach(function (s) { secById[s.id] = s; });

    var head = el('div', 'panel-head');
    var h2 = el('h2', null, b.title);
    h2.appendChild(tagPills(b.tags, 'tag'));
    head.appendChild(h2);
    head.appendChild(el('span', 'when num', b.start + ' to ' + b.end + ', ' + b.min + ' min'));
    panel.appendChild(head);

    var actions = el('div', 'actions');
    var listBtn = el('button', 'btn quiet listbtn', 'Blocks');
    listBtn.setAttribute('type', 'button');
    listBtn.addEventListener('click', function () { document.body.classList.toggle('show-list'); });
    actions.appendChild(listBtn);
    if (x.status === 'running') {
      var doneBtn = el('button', 'btn', 'Done');
      doneBtn.setAttribute('type', 'button');
      doneBtn.addEventListener('click', function () { ROS.end(state, b.id, nowIso()); commit(); });
      actions.appendChild(doneBtn);
      var reBtn = el('button', 'btn quiet', 'Restart');
      reBtn.setAttribute('type', 'button');
      reBtn.addEventListener('click', function () { confirmTap(reBtn, 'restart', 'Restart', function () { ROS.restart(state, b.id, nowIso()); commit(); }); });
      actions.appendChild(reBtn);
    } else {
      var startBtn = el('button', 'btn', x.status === 'done' ? 'Start again' : 'Start');
      startBtn.setAttribute('type', 'button');
      startBtn.addEventListener('click', function () {
        ui.wanted = true; wake();
        if (x.status === 'done') { confirmTap(startBtn, 'restart', 'Start again', function () { ROS.restart(state, b.id, nowIso()); commit(); }); return; }
        ROS.start(state, b.id, nowIso()); commit();
      });
      actions.appendChild(startBtn);
    }
    if (x.startedAt) {
      var line = x.status === 'done'
        ? 'Ran ' + ROS.clockIn(x.startedAt, TZ) + ' to ' + ROS.clockIn(x.endedAt, TZ) + ', ' + x.actualMin + ' of ' + b.min + ' min'
        : 'Started ' + ROS.clockIn(x.startedAt, TZ);
      if (x.startDrift !== null) line += ' (' + driftWord(x.startDrift, 'late', 'early') + ')';
      if (x.status === 'done' && x.endDrift !== null) line += ', ended ' + driftWord(x.endDrift, 'behind', 'ahead');
      var status = el('span', 'intro num', line + '.');
      status.style.alignSelf = 'center';
      actions.appendChild(status);
    }
    panel.appendChild(actions);

    (b.intro || []).forEach(function (html) { var p = el('p', 'intro'); p.innerHTML = html; panel.appendChild(p); });
    if (b.breakQuestion) {
      var q = el('div', 'question');
      q.appendChild(document.createTextNode(b.breakQuestion.question));
      if (b.breakQuestion.opens) q.appendChild(el('small', null, 'Opens the next block as: ' + b.breakQuestion.opens));
      panel.appendChild(q);
    }
    if (b.slides && b.slides.length) {
      panel.appendChild(el('p', 'slides', 'Slides: ' + b.slides.join(' → ')));
    }

    if (b.rows.length) {
      var sum = 0, done = 0;
      b.rows.forEach(function (r) { if (r.min) sum += r.min; if (state.ticks[r.id]) done++; });
      var sumLine = el('div', 'sum');
      sumLine.appendChild(el('span', null, done + ' of ' + b.rows.length + ' done'));
      sumLine.appendChild(el('span', 'num', sum ? 'rows add up to ' + sum + ' min' : ''));
      panel.appendChild(sumLine);

      var rows = el('ul', 'rows');
      b.rows.forEach(function (r) {
        var li = el('li', 'row' + (state.ticks[r.id] ? ' done' : '') + (ui.open[r.id] ? ' expanded' : ''));
        var line = el('div', 'row-line');
        var tb = el('button', 'tick', '✓');
        tb.setAttribute('type', 'button'); tb.setAttribute('aria-pressed', state.ticks[r.id] ? 'true' : 'false'); tb.setAttribute('aria-label', 'done');
        tb.addEventListener('click', function () { ROS.toggle(state, r.id, nowIso()); commit(); });
        line.appendChild(tb);
        line.appendChild(el('span', 'min num', r.min ? r.min : ''));
        var hasNotes = (r.sections && r.sections.length) || r.question;
        var lab = el('button', 'label' + (hasNotes ? '' : ' static'));
        lab.setAttribute('type', 'button');
        lab.appendChild(inlineHtml(r.html || r.label));
        if (hasNotes) {
          lab.appendChild(el('span', 'chev', '›'));
          lab.setAttribute('aria-expanded', ui.open[r.id] ? 'true' : 'false');
          lab.addEventListener('click', function () {
            if (ui.open[r.id]) delete ui.open[r.id]; else ui.open[r.id] = true;
            saveUi(); renderAll();
          });
        } else {
          lab.disabled = true;
        }
        line.appendChild(lab);
        li.appendChild(line);
        if (hasNotes) {
          var notes = el('div', 'notes');
          notes.hidden = !ui.open[r.id];
          if (r.question) {
            var oq = el('div', 'question');
            oq.appendChild(document.createTextNode(r.question));
            oq.appendChild(el('small', null, 'The question that went into the break. Two answers, then on.'));
            notes.appendChild(oq);
          }
          r.sections.forEach(function (sid) { if (secById[sid]) notes.appendChild(renderSection(secById[sid], b.id)); });
          li.appendChild(notes);
        }
        rows.appendChild(li);
      });
      panel.appendChild(rows);
    }
    if (b.orphanSections && b.orphanSections.length) {
      panel.appendChild(el('div', 'sec more', 'More notes'));
      b.orphanSections.forEach(function (sid) { if (secById[sid]) panel.appendChild(renderSection(secById[sid], b.id)); });
    }
  }

  function renderChecks(items, container) {
    container.innerHTML = '';
    items.forEach(function (it) {
      var li = el('li', state.ticks[it.id] ? 'done' : '');
      var tb = el('button', 'tick', '✓');
      tb.setAttribute('type', 'button'); tb.setAttribute('aria-pressed', state.ticks[it.id] ? 'true' : 'false'); tb.setAttribute('aria-label', 'done');
      tb.addEventListener('click', function () { ROS.toggle(state, it.id, nowIso()); commit(); });
      li.appendChild(tb);
      var txt = el('span', 'txt'); txt.innerHTML = it.html; li.appendChild(txt);
      container.appendChild(li);
    });
  }

  function renderPlain(items, container) {
    container.innerHTML = '';
    items.forEach(function (html) { var li = el('li'); li.innerHTML = html; container.appendChild(li); });
  }

  function renderLog(d) {
    var tb = $('#logbody');
    tb.innerHTML = '';
    data.blocks.forEach(function (b) {
      var x = d.blocks[b.id];
      var tr = el('tr');
      tr.appendChild(el('td', null, b.title));
      tr.appendChild(el('td', 'num', b.start + ' to ' + b.end));
      tr.appendChild(el('td', 'num', x.startedAt ? ROS.clockIn(x.startedAt, TZ) + (x.endedAt ? ' to ' + ROS.clockIn(x.endedAt, TZ) : ', running') : ''));
      tr.appendChild(el('td', 'n num', x.actualMin !== null ? x.actualMin + ' of ' + b.min : (x.startedAt ? 'of ' + b.min : String(b.min))));
      var td = el('td', 'n num' + (x.endDrift !== null && x.endDrift > 0 ? ' behind' : ''), x.endDrift === null ? '' : (x.endDrift > 0 ? '+' + x.endDrift : String(x.endDrift)));
      tr.appendChild(td);
      tb.appendChild(tr);
    });
    var n = Object.keys(state.ticks).length;
    $('#tickcount').textContent = n + (n === 1 ? ' tick' : ' ticks') + ' recorded';
  }

  function renderAll() {
    var d = ROS.derive(data, state, Date.now());
    renderHeader();
    document.querySelectorAll('nav.tabs button').forEach(function (bt) { bt.setAttribute('aria-selected', bt.dataset.tab === ui.tab ? 'true' : 'false'); });
    document.querySelectorAll('.tab').forEach(function (t) { t.hidden = t.id !== 'tab-' + ui.tab; });
    if (ui.tab === 'day') { renderBlocks(d); renderPanel(d); }
    if (ui.tab === 'before') { renderChecks(data.lists.before, $('#beforelist')); renderChecks(data.lists.arrival, $('#arrivallist')); }
    if (ui.tab === 'after') renderChecks(data.lists.after, $('#afterlist'));
    if (ui.tab === 'log') renderLog(d);
  }

  function tickUI() {
    if (!state) return;
    renderHeader();
    if (ui.tab === 'day') {
      var d = ROS.derive(data, state, Date.now());
      if (d.runningId) {
        var x = d.blocks[d.runningId];
        var blk = document.querySelector('#blocks .blk.running .sub');
        if (blk) blk.textContent = 'running, ' + ROS.fmtDur(x.running) + (x.over ? ' (over)' : ' of ' + byId[d.runningId].min + ' min');
      }
    }
  }

  /* ---------- boot ---------- */

  function boot() {
    device = (function () { try { var k = 'ros:device'; var v = localStorage.getItem(k); if (!v) { v = 'd' + Math.random().toString(36).slice(2, 8); localStorage.setItem(k, v); } return v; } catch (e) { return null; } })();
    loadUi();
    state = loadState();

    // static parts
    renderPlain(data.rules, $('#ruleslist'));
    renderPlain(data.materials, $('#materialslist'));
    $('#stamp').textContent = 'Built from lesson-plan.qmd, ' + data.source.builtAt + ' (sha256 ' + data.source.sha256.slice(0, 12) + '). Workshop date ' + data.workshopDate + ', clock in ' + TZ + '.';

    document.querySelectorAll('nav.tabs button').forEach(function (bt) {
      bt.addEventListener('click', function () { ui.tab = bt.dataset.tab; saveUi(); renderAll(); });
    });
    $('#copybtn').addEventListener('click', function () {
      var text = JSON.stringify(ROS.exportLog(data, state, Date.now()), null, 2);
      var box = $('#exportbox');
      var showBox = function () { box.hidden = false; box.value = text; box.focus(); box.select(); };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () { $('#copybtn').textContent = 'Copied'; setTimeout(function () { $('#copybtn').textContent = 'Copy log'; }, 2000); }, showBox);
      } else { showBox(); }
    });
    var resetBtn = $('#resetbtn');
    resetBtn.addEventListener('click', function () { confirmTap(resetBtn, 'reset', 'Reset day', function () { ROS.reset(state, nowIso()); commit(); }); });

    setSync('local'); setWake(false);
    renderAll();
    setInterval(tickUI, 1000);
    document.addEventListener('visibilitychange', function () { if (document.visibilityState === 'visible') { wake(); tickUI(); } });
    window.addEventListener('storage', function (ev) { if (ev.key === KEY && !dbRef) { state = loadState(); renderAll(); } });
    document.addEventListener('click', function () { if (ui.wanted && !wakeLock) wake(); }, true);
    connectDb();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
})();
