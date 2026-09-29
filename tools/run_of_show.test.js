// Unit tests for the pure part of the run of show app.
// Run: node --test tools/run_of_show.test.js
'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const ROS = require('./run_of_show.js');

const data = {
  workshopDate: '2026-09-29',
  timeZone: 'Europe/Zurich',
  blocks: [
    { id: 'b0900', title: 'Opening', start: '09:00', end: '09:40', min: 40, startIso: '2026-09-29T09:00:00+02:00', endIso: '2026-09-29T09:40:00+02:00', rows: [{ id: 'b0900/r0', label: 'Welcome', min: 3 }], sections: [] },
    { id: 'b0940', title: 'Rails', start: '09:40', end: '10:15', min: 35, startIso: '2026-09-29T09:40:00+02:00', endIso: '2026-09-29T10:15:00+02:00', rows: [], sections: [] },
    { id: 'b1015', title: 'Break', start: '10:15', end: '10:35', min: 20, startIso: '2026-09-29T10:15:00+02:00', endIso: '2026-09-29T10:35:00+02:00', rows: [], sections: [] },
  ],
  lists: { before: [], arrival: [], after: [] },
};
const T = (s) => Date.parse(s);

test('fmtDur', () => {
  assert.equal(ROS.fmtDur(0), '0:00');
  assert.equal(ROS.fmtDur(65), '1:05');
  assert.equal(ROS.fmtDur(3725), '1:02:05');
  assert.equal(ROS.fmtDur(-90), '-1:30');
});

test('live day: running, left, drift against the printed clock', () => {
  const st = ROS.blankState('2026-09-29', 'dev');
  ROS.start(st, 'b0900', '2026-09-29T07:03:00.000Z'); // 09:03 local, 3 min late
  const d = ROS.derive(data, st, T('2026-09-29T07:15:00Z')); // 09:15
  assert.equal(d.live, true);
  assert.equal(d.runningId, 'b0900');
  assert.equal(d.nextId, 'b0940');
  const x = d.blocks.b0900;
  assert.equal(x.status, 'running');
  assert.equal(x.running, 12 * 60);
  assert.equal(x.left, 28 * 60);
  assert.equal(x.over, false);
  assert.equal(x.startDrift, 3);
  assert.equal(x.endDrift, 3); // projected end 09:43 against 09:40
});

test('over time counts up and starting the next block ends the running one', () => {
  const st = ROS.blankState('2026-09-29', 'dev');
  ROS.start(st, 'b0900', '2026-09-29T07:00:00.000Z');
  let d = ROS.derive(data, st, T('2026-09-29T07:45:00Z')); // 09:45, block planned to end 09:40
  assert.equal(d.blocks.b0900.over, true);
  assert.equal(d.blocks.b0900.left, -5 * 60);
  assert.equal(d.blocks.b0900.endDrift, 5);
  ROS.start(st, 'b0940', '2026-09-29T07:46:00.000Z');
  d = ROS.derive(data, st, T('2026-09-29T07:50:00Z'));
  assert.equal(d.blocks.b0900.status, 'done');
  assert.equal(d.blocks.b0900.actualMin, 46);
  assert.equal(d.runningId, 'b0940');
  assert.equal(d.blocks.b0940.startDrift, 6);
  assert.equal(d.nextId, 'b1015');
});

test('rehearsal day: drift against planned durations from the first tap', () => {
  const st = ROS.blankState('2026-10-03', 'dev');
  ROS.start(st, 'b0900', '2026-10-03T12:00:00.000Z');
  ROS.start(st, 'b0940', '2026-10-03T12:50:00.000Z'); // planned offset 40 min, actual 50
  const d = ROS.derive(data, st, T('2026-10-03T12:55:00Z'));
  assert.equal(d.live, false);
  assert.equal(d.blocks.b0900.startDrift, 0);
  assert.equal(d.blocks.b0900.endDrift, 10);
  assert.equal(d.blocks.b0940.startDrift, 10);
  assert.equal(d.blocks.b0940.left, 30 * 60);
});

test('out of order start, done, restart, ticks and reset', () => {
  const st = ROS.blankState('2026-09-29', 'dev');
  ROS.start(st, 'b0940', '2026-09-29T07:00:00.000Z');
  let d = ROS.derive(data, st, T('2026-09-29T07:01:00Z'));
  assert.equal(d.runningId, 'b0940');
  assert.equal(d.nextId, 'b1015');
  ROS.end(st, 'b0940', '2026-09-29T07:30:00.000Z');
  d = ROS.derive(data, st, T('2026-09-29T07:31:00Z'));
  assert.equal(d.runningId, null);
  assert.equal(d.blocks.b0940.actualMin, 30);
  ROS.restart(st, 'b0940', '2026-09-29T07:32:00.000Z');
  d = ROS.derive(data, st, T('2026-09-29T07:33:00Z'));
  assert.equal(d.blocks.b0940.status, 'running');
  assert.equal(d.blocks.b0940.running, 60);
  ROS.toggle(st, 'b0900/r0', '2026-09-29T07:34:00.000Z');
  assert.ok(st.ticks['b0900/r0']);
  ROS.toggle(st, 'b0900/r0', '2026-09-29T07:35:00.000Z');
  assert.equal(st.ticks['b0900/r0'], undefined);
  ROS.toggle(st, 'b0900/r0', '2026-09-29T07:36:00.000Z');
  ROS.reset(st, '2026-09-29T07:40:00.000Z');
  assert.deepEqual(st.blocks, {});
  assert.deepEqual(st.ticks, {});
  assert.equal(st.updatedAt, '2026-09-29T07:40:00.000Z');
});

test('export log lists blocks and ticks with minutes into the block', () => {
  const st = ROS.blankState('2026-09-29', 'dev');
  ROS.start(st, 'b0900', '2026-09-29T07:00:00.000Z');
  ROS.toggle(st, 'b0900/r0', '2026-09-29T07:04:00.000Z');
  const log = ROS.exportLog(data, st, T('2026-09-29T07:10:00Z'));
  assert.equal(log.blocks.length, 3);
  assert.equal(log.blocks[0].startedAt, '2026-09-29T07:00:00.000Z');
  assert.equal(log.ticks.length, 1);
  assert.equal(log.ticks[0].label, 'Welcome');
  assert.equal(log.ticks[0].minIntoBlock, 4);
});
