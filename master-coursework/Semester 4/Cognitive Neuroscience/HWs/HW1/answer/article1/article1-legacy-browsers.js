/***************** 
 * Article1 *
 *****************/


// store info about the experiment session:
let expName = 'article1';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
    'learning type': '1',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('white'),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(text_0RoutineBegin());
flowScheduler.add(text_0RoutineEachFrame());
flowScheduler.add(text_0RoutineEnd());
const training_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(training_trialsLoopBegin(training_trialsLoopScheduler));
flowScheduler.add(training_trialsLoopScheduler);
flowScheduler.add(training_trialsLoopEnd);



flowScheduler.add(text_1RoutineBegin());
flowScheduler.add(text_1RoutineEachFrame());
flowScheduler.add(text_1RoutineEnd());
const learning_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(learning_trialsLoopBegin(learning_trialsLoopScheduler));
flowScheduler.add(learning_trialsLoopScheduler);
flowScheduler.add(learning_trialsLoopEnd);



flowScheduler.add(text_2RoutineBegin());
flowScheduler.add(text_2RoutineEachFrame());
flowScheduler.add(text_2RoutineEnd());
const transfer_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(transfer_trialsLoopBegin(transfer_trialsLoopScheduler));
flowScheduler.add(transfer_trialsLoopScheduler);
flowScheduler.add(transfer_trialsLoopEnd);




flowScheduler.add(text_3RoutineBegin());
flowScheduler.add(text_3RoutineEachFrame());
flowScheduler.add(text_3RoutineEnd());
const estimation_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(estimation_trialsLoopBegin(estimation_trialsLoopScheduler));
flowScheduler.add(estimation_trialsLoopScheduler);
flowScheduler.add(estimation_trialsLoopEnd);



flowScheduler.add(show_rewardRoutineBegin());
flowScheduler.add(show_rewardRoutineEachFrame());
flowScheduler.add(show_rewardRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.WARNING);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.1.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "text_0"
  text_0Clock = new util.Clock();
  text0 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text0',
    text: 'هر بار از میان دو گزینه\u200cی نمایش داده شده،\nبا فشردن یکی از کلیدهای راست و چپ روی کیبورد،\n گزینه\u200cی با بیشترین پاداش را انتخاب کنید.\n\n(هرگاه آماده بودید، کلید space را فشار دهید.)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  text0_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation_training"
  fixation_trainingClock = new util.Clock();
  fixation0 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation0', units : 'norm', 
    vertices: 'cross', size:[0.03, 0.06],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 0.08, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color('black'),
    fillColor: 'black',
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "main_training"
  main_trainingClock = new util.Clock();
  // Run 'Begin Experiment' code from training_code
  import * as random from 'random';
  image_pairs0 = [["1-1.jpg", "1-2.jpg"], ["1-3.jpg", "1-4.jpg"], ["1-2.jpg", "1-1.jpg"], ["1-4.jpg", "1-3.jpg"]];
  trials0 = [];
  for (var pair, _pj_c = 0, _pj_a = image_pairs0, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
      pair = _pj_a[_pj_c];
      trials0.push(pair);
  }
  trials0 *= 5;
  Math.random.shuffle(trials0);
  current_trial0 = 0;
  
  left_image_0 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'left_image_0', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.5), 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  right_image_0 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'right_image_0', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.5, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  key_resp_0 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from code_0
  import * as np from 'numpy';
  pos_k0 = [0, 0];
  l_type = expInfo["learning type"];
  
  polygon_0 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_0', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 20.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 0.5765), 0.0039, 1.0]),
    fillColor: new util.Color([0.0, 0.0, 0.0]),
    fillColor: [0.0, 0.0, 0.0],
    opacity: 0.3, depth: -5, interpolate: true,
  });
  
  left_learning_reward_0 = new visual.TextBox({
    win: psychoJS.window,
    name: 'left_learning_reward_0',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [(- 0.5), (- 0.3)], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.6, 0.6],  units: undefined, 
    color: [(- 0.5765), 0.0039, 1.0], colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -6.0 
  });
  
  right_learning_reward_0 = new visual.TextBox({
    win: psychoJS.window,
    name: 'right_learning_reward_0',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0.5, (- 0.3)], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.6, 0.6],  units: undefined, 
    color: [(- 0.5765), 0.0039, 1.0], colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -7.0 
  });
  
  text_no_resp_0 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_no_resp_0',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -8.0 
  });
  
  // Initialize components for Routine "text_1"
  text_1Clock = new util.Clock();
  text1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text1',
    text: 'هر بار از میان دو گزینه\u200cی نمایش داده شده،\nبا فشردن یکی از کلیدهای راست و چپ روی کیبورد،\n گزینه\u200cی با بیشترین پاداش را انتخاب کنید.\n\n(مجموع پاداش\u200cهای شما در این بخش،\nپاداش نهایی شما را تعیین خواهد کرد.)\n\n(هرگاه آماده بودید، کلید space را فشار دهید.)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  text1_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation_learning"
  fixation_learningClock = new util.Clock();
  fixation1 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation1', units : 'norm', 
    vertices: 'cross', size:[0.03, 0.06],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 0.08, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color('black'),
    fillColor: 'black',
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "main_learning"
  main_learningClock = new util.Clock();
  // Run 'Begin Experiment' code from learning_code
  import * as random from 'random';
  image_pairs = [["1.jpg", "2.jpg"], ["3.jpg", "4.jpg"], ["2.jpg", "1.jpg"], ["4.jpg", "3.jpg"]];
  trials = [];
  for (var pair, _pj_c = 0, _pj_a = image_pairs, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
      pair = _pj_a[_pj_c];
      trials.push(pair);
  }
  trials *= 25;
  Math.random.shuffle(trials);
  current_trial = 0;
  
  left_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'left_image', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.5), 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  right_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'right_image', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.5, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from code
  import * as np from 'numpy';
  pos_k = [0, 0];
  l_type = expInfo["learning type"];
  total_reward = 0;
  
  polygon = new visual.Rect ({
    win: psychoJS.window, name: 'polygon', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 20.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 0.5765), 0.0039, 1.0]),
    fillColor: new util.Color([0.0, 0.0, 0.0]),
    fillColor: [0.0, 0.0, 0.0],
    opacity: 0.3, depth: -5, interpolate: true,
  });
  
  left_learning_reward = new visual.TextBox({
    win: psychoJS.window,
    name: 'left_learning_reward',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [(- 0.5), (- 0.3)], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.6, 0.6],  units: undefined, 
    color: [(- 0.5765), 0.0039, 1.0], colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -6.0 
  });
  
  right_learning_reward = new visual.TextBox({
    win: psychoJS.window,
    name: 'right_learning_reward',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0.5, (- 0.3)], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.6, 0.6],  units: undefined, 
    color: [(- 0.5765), 0.0039, 1.0], colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -7.0 
  });
  
  text_no_resp = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_no_resp',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -8.0 
  });
  
  // Initialize components for Routine "text_2"
  text_2Clock = new util.Clock();
  text2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text2',
    text: 'هر بار از میان دو گزینه\u200cی نمایش داده شده،\nبا فشردن یکی از کلیدهای راست و چپ روی کیبورد،\n گزینه\u200cی با بیشترین پاداش را انتخاب کنید.\n\nتوجه:\nدر این بخش ممکن است جفت عددهایی را مقایسه کنید \nکه در بخش قبل مقایسه نکرده بودید.\n\nپس از انتخاب یکی از دو گزینه\u200cی نمایش داده شده\nباید میزان اطمینان خود از انتخابتان را با استفاده از موس\nمشخص کنید.\n\n(هرگاه آماده بودید، کلید space را فشار دهید.)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  text2_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation_transfer"
  fixation_transferClock = new util.Clock();
  fixation2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation2', units : 'norm', 
    vertices: 'cross', size:[0.03, 0.06],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 0.08, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color('black'),
    fillColor: 'black',
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "main_transfer"
  main_transferClock = new util.Clock();
  // Run 'Begin Experiment' code from transfer_code
  import * as random from 'random';
  image_pairs_2 = [["1.jpg", "2.jpg"], ["1.jpg", "3.jpg"], ["1.jpg", "4.jpg"], ["2.jpg", "3.jpg"], ["2.jpg", "4.jpg"], ["3.jpg", "4.jpg"]];
  trials_2 = [];
  for (var pair, _pj_c = 0, _pj_a = image_pairs_2, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
      pair = _pj_a[_pj_c];
      trials_2.push(pair);
  }
  trials_2 *= 4;
  Math.random.shuffle(trials_2);
  current_trial_2 = 0;
  
  left_image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'left_image_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.5), 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  right_image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'right_image_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.5, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from code_2
  import * as np from 'numpy';
  pos_k_2 = [0, 0];
  
  polygon_2 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_2', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 20.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 0.5765), 0.0039, 1.0]),
    fillColor: new util.Color([0.0, 0.0, 0.0]),
    fillColor: [0.0, 0.0, 0.0],
    opacity: 0.3, depth: -5, interpolate: true,
  });
  
  // Initialize components for Routine "slider_transfer"
  slider_transferClock = new util.Clock();
  slider_trns = new visual.Slider({
    win: psychoJS.window, name: 'slider_trns',
    startValue: 50,
    size: [1.0, 0.1], pos: [0, 0], ori: 0.0, units: psychoJS.window.units,
    labels: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], fontSize: 0.05, ticks: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    granularity: 5.0, style: ["SLIDER"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('Black'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: 0, 
    flip: false,
  });
  
  mouse_trns = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_trns.mouseClock = new util.Clock();
  // Initialize components for Routine "text_3"
  text_3Clock = new util.Clock();
  text3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text3',
    text: 'برای هر تصویر نمایش داده شده\nمیزان برآورد خود از پاداش مربوط به آن را \nبا استفاده از موس مشخص کنید.\n\n(هرگاه آماده بودید، کلید space را فشار دهید.)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  text3_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation_estimation"
  fixation_estimationClock = new util.Clock();
  fixation3 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation3', units : 'norm', 
    vertices: 'cross', size:[0.03, 0.06],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 0.08, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color('black'),
    fillColor: 'black',
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "main_estimation"
  main_estimationClock = new util.Clock();
  // Run 'Begin Experiment' code from estimation_code
  import * as random from 'random';
  images3 = ["1.jpg", "2.jpg", "3.jpg", "4.jpg"];
  trials_3 = [];
  for (var image, _pj_c = 0, _pj_a = images3, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
      image = _pj_a[_pj_c];
      trials_3.push(image);
  }
  trials_3 *= 4;
  Math.random.shuffle(trials_3);
  current_trial_3 = 0;
  
  image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_3', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.2], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  slider_estm = new visual.Slider({
    win: psychoJS.window, name: 'slider_estm',
    startValue: 50,
    size: [1.0, 0.1], pos: [0, (- 0.2)], ori: 0.0, units: psychoJS.window.units,
    labels: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], fontSize: 0.05, ticks: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    granularity: 5.0, style: ["SLIDER"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('Black'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -2, 
    flip: false,
  });
  
  mouse_estm = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_estm.mouseClock = new util.Clock();
  // Initialize components for Routine "show_reward"
  show_rewardClock = new util.Clock();
  text4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text4',
    text: 'مجموع پاداش\u200c (با توجه به گزینه\u200cهای فاز یادگیری):\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  totalRewardText = new visual.TextStim({
    win: psychoJS.window,
    name: 'totalRewardText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.1)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function text_0RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'text_0' ---
    t = 0;
    text_0Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('text_0.started', globalClock.getTime());
    text0_key_resp.keys = undefined;
    text0_key_resp.rt = undefined;
    _text0_key_resp_allKeys = [];
    // keep track of which components have finished
    text_0Components = [];
    text_0Components.push(text0);
    text_0Components.push(text0_key_resp);
    
    text_0Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function text_0RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'text_0' ---
    // get current time
    t = text_0Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text0* updates
    if (t >= 0.0 && text0.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text0.tStart = t;  // (not accounting for frame time here)
      text0.frameNStart = frameN;  // exact frame index
      
      text0.setAutoDraw(true);
    }
    
    
    // *text0_key_resp* updates
    if (t >= 0.0 && text0_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text0_key_resp.tStart = t;  // (not accounting for frame time here)
      text0_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { text0_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { text0_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { text0_key_resp.clearEvents(); });
    }
    
    if (text0_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = text0_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _text0_key_resp_allKeys = _text0_key_resp_allKeys.concat(theseKeys);
      if (_text0_key_resp_allKeys.length > 0) {
        text0_key_resp.keys = _text0_key_resp_allKeys[_text0_key_resp_allKeys.length - 1].name;  // just the last key pressed
        text0_key_resp.rt = _text0_key_resp_allKeys[_text0_key_resp_allKeys.length - 1].rt;
        text0_key_resp.duration = _text0_key_resp_allKeys[_text0_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    text_0Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function text_0RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'text_0' ---
    text_0Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('text_0.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(text0_key_resp.corr, level);
    }
    psychoJS.experiment.addData('text0_key_resp.keys', text0_key_resp.keys);
    if (typeof text0_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('text0_key_resp.rt', text0_key_resp.rt);
        psychoJS.experiment.addData('text0_key_resp.duration', text0_key_resp.duration);
        routineTimer.reset();
        }
    
    text0_key_resp.stop();
    // the Routine "text_0" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function training_trialsLoopBegin(training_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    training_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'training_trials'
    });
    psychoJS.experiment.addLoop(training_trials); // add the loop to the experiment
    currentLoop = training_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    training_trials.forEach(function() {
      snapshot = training_trials.getSnapshot();
    
      training_trialsLoopScheduler.add(importConditions(snapshot));
      training_trialsLoopScheduler.add(fixation_trainingRoutineBegin(snapshot));
      training_trialsLoopScheduler.add(fixation_trainingRoutineEachFrame());
      training_trialsLoopScheduler.add(fixation_trainingRoutineEnd(snapshot));
      training_trialsLoopScheduler.add(main_trainingRoutineBegin(snapshot));
      training_trialsLoopScheduler.add(main_trainingRoutineEachFrame());
      training_trialsLoopScheduler.add(main_trainingRoutineEnd(snapshot));
      training_trialsLoopScheduler.add(training_trialsLoopEndIteration(training_trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function training_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(training_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function training_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function learning_trialsLoopBegin(learning_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    learning_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'learning_trials'
    });
    psychoJS.experiment.addLoop(learning_trials); // add the loop to the experiment
    currentLoop = learning_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    learning_trials.forEach(function() {
      snapshot = learning_trials.getSnapshot();
    
      learning_trialsLoopScheduler.add(importConditions(snapshot));
      learning_trialsLoopScheduler.add(fixation_learningRoutineBegin(snapshot));
      learning_trialsLoopScheduler.add(fixation_learningRoutineEachFrame());
      learning_trialsLoopScheduler.add(fixation_learningRoutineEnd(snapshot));
      learning_trialsLoopScheduler.add(main_learningRoutineBegin(snapshot));
      learning_trialsLoopScheduler.add(main_learningRoutineEachFrame());
      learning_trialsLoopScheduler.add(main_learningRoutineEnd(snapshot));
      learning_trialsLoopScheduler.add(learning_trialsLoopEndIteration(learning_trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function learning_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(learning_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function learning_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function transfer_trialsLoopBegin(transfer_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    transfer_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'transfer_trials'
    });
    psychoJS.experiment.addLoop(transfer_trials); // add the loop to the experiment
    currentLoop = transfer_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    transfer_trials.forEach(function() {
      snapshot = transfer_trials.getSnapshot();
    
      transfer_trialsLoopScheduler.add(importConditions(snapshot));
      transfer_trialsLoopScheduler.add(fixation_transferRoutineBegin(snapshot));
      transfer_trialsLoopScheduler.add(fixation_transferRoutineEachFrame());
      transfer_trialsLoopScheduler.add(fixation_transferRoutineEnd(snapshot));
      transfer_trialsLoopScheduler.add(main_transferRoutineBegin(snapshot));
      transfer_trialsLoopScheduler.add(main_transferRoutineEachFrame());
      transfer_trialsLoopScheduler.add(main_transferRoutineEnd(snapshot));
      transfer_trialsLoopScheduler.add(slider_transferRoutineBegin(snapshot));
      transfer_trialsLoopScheduler.add(slider_transferRoutineEachFrame());
      transfer_trialsLoopScheduler.add(slider_transferRoutineEnd(snapshot));
      transfer_trialsLoopScheduler.add(transfer_trialsLoopEndIteration(transfer_trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function transfer_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(transfer_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function transfer_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function estimation_trialsLoopBegin(estimation_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    estimation_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'estimation_trials'
    });
    psychoJS.experiment.addLoop(estimation_trials); // add the loop to the experiment
    currentLoop = estimation_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    estimation_trials.forEach(function() {
      snapshot = estimation_trials.getSnapshot();
    
      estimation_trialsLoopScheduler.add(importConditions(snapshot));
      estimation_trialsLoopScheduler.add(fixation_estimationRoutineBegin(snapshot));
      estimation_trialsLoopScheduler.add(fixation_estimationRoutineEachFrame());
      estimation_trialsLoopScheduler.add(fixation_estimationRoutineEnd(snapshot));
      estimation_trialsLoopScheduler.add(main_estimationRoutineBegin(snapshot));
      estimation_trialsLoopScheduler.add(main_estimationRoutineEachFrame());
      estimation_trialsLoopScheduler.add(main_estimationRoutineEnd(snapshot));
      estimation_trialsLoopScheduler.add(estimation_trialsLoopEndIteration(estimation_trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function estimation_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(estimation_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function estimation_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function fixation_trainingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixation_training' ---
    t = 0;
    fixation_trainingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('fixation_training.started', globalClock.getTime());
    // keep track of which components have finished
    fixation_trainingComponents = [];
    fixation_trainingComponents.push(fixation0);
    
    fixation_trainingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function fixation_trainingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixation_training' ---
    // get current time
    t = fixation_trainingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation0* updates
    if (t >= 0.0 && fixation0.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation0.tStart = t;  // (not accounting for frame time here)
      fixation0.frameNStart = frameN;  // exact frame index
      
      fixation0.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation0.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation0.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixation_trainingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function fixation_trainingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixation_training' ---
    fixation_trainingComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('fixation_training.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function main_trainingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'main_training' ---
    t = 0;
    main_trainingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('main_training.started', globalClock.getTime());
    // Run 'Begin Routine' code from training_code
    leftimage_0 = trials0[current_trial0][0];
    rightimage_0 = trials0[current_trial0][1];
    current_trial0 += 1;
    
    left_image_0.setImage(leftimage_0);
    right_image_0.setImage(rightimage_0);
    key_resp_0.keys = undefined;
    key_resp_0.rt = undefined;
    _key_resp_0_allKeys = [];
    // Run 'Begin Routine' code from code_0
    sample_A1 = (- 1);
    sample_B = (- 1);
    sample_A2 = (- 1);
    sample_C = (- 1);
    while (((sample_A1 < 0) || (sample_A1 > 100))) {
        sample_A1 = np.random.normal(64, 13, 1)[0];
    }
    while (((sample_B < 0) || (sample_A1 > 100))) {
        sample_B = np.random.normal(54, 13, 1)[0];
    }
    while (((sample_A2 < 0) || (sample_A1 > 100))) {
        sample_A2 = np.random.normal(64, 13, 1)[0];
    }
    while (((sample_C < 0) || (sample_A1 > 100))) {
        sample_C = np.random.normal(44, 13, 1)[0];
    }
    no_response = false;
    routineStartTime = t;
    
    left_learning_reward_0.setText('');
    right_learning_reward_0.setText('');
    // keep track of which components have finished
    main_trainingComponents = [];
    main_trainingComponents.push(left_image_0);
    main_trainingComponents.push(right_image_0);
    main_trainingComponents.push(key_resp_0);
    main_trainingComponents.push(polygon_0);
    main_trainingComponents.push(left_learning_reward_0);
    main_trainingComponents.push(right_learning_reward_0);
    main_trainingComponents.push(text_no_resp_0);
    
    main_trainingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function main_trainingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'main_training' ---
    // get current time
    t = main_trainingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *left_image_0* updates
    if (t >= 0 && left_image_0.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      left_image_0.tStart = t;  // (not accounting for frame time here)
      left_image_0.frameNStart = frameN;  // exact frame index
      
      left_image_0.setAutoDraw(true);
    }
    
    frameRemains = 0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (left_image_0.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      left_image_0.setAutoDraw(false);
    }
    
    
    // *right_image_0* updates
    if (t >= 0 && right_image_0.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      right_image_0.tStart = t;  // (not accounting for frame time here)
      right_image_0.frameNStart = frameN;  // exact frame index
      
      right_image_0.setAutoDraw(true);
    }
    
    frameRemains = 0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (right_image_0.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      right_image_0.setAutoDraw(false);
    }
    
    
    // *key_resp_0* updates
    if (t >= 0 && key_resp_0.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_0.tStart = t;  // (not accounting for frame time here)
      key_resp_0.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_0.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_0.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_0.clearEvents(); });
    }
    
    frameRemains = 0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_0.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_0.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_resp_0.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_0.getKeys({keyList: ['right', 'left'], waitRelease: false});
      _key_resp_0_allKeys = _key_resp_0_allKeys.concat(theseKeys);
      if (_key_resp_0_allKeys.length > 0) {
        key_resp_0.keys = _key_resp_0_allKeys[_key_resp_0_allKeys.length - 1].name;  // just the last key pressed
        key_resp_0.rt = _key_resp_0_allKeys[_key_resp_0_allKeys.length - 1].rt;
        key_resp_0.duration = _key_resp_0_allKeys[_key_resp_0_allKeys.length - 1].duration;
      }
    }
    
    // Run 'Each Frame' code from code_0
    if ((trials0[(current_trial0 - 1)][0] === "1-1.jpg")) {
        reward_A1 = Number.parseInt(util.round(sample_A1));
        if ((l_type === "1")) {
            com_par_time = 1;
            if ((key_resp_0.keys === "left")) {
                left_learning_reward_0.text = `Reward: ${reward_A1}`;
            } else {
                if ((key_resp_0.keys === "right")) {
                    left_learning_reward_0.text = "";
                }
            }
        } else {
            if ((l_type === "2")) {
                com_par_time = 0.5;
                if ((key_resp_0.keys === "left")) {
                    left_learning_reward_0.text = `Reward: ${reward_A1}`;
                } else {
                    if ((key_resp_0.keys === "right")) {
                        left_learning_reward_0.text = "";
                    }
                }
            }
        }
        reward_B = Number.parseInt(util.round(sample_B));
        if ((l_type === "1")) {
            com_par_time = 1;
            if ((key_resp_0.keys === "right")) {
                right_learning_reward_0.text = `Reward: ${reward_B}`;
            } else {
                if ((key_resp_0.keys === "left")) {
                    right_learning_reward_0.text = "";
                }
            }
        } else {
            if ((l_type === "2")) {
                com_par_time = 0.5;
                if ((key_resp_0.keys === "right")) {
                    right_learning_reward_0.text = `Reward: ${reward_B}`;
                } else {
                    if ((key_resp_0.keys === "left")) {
                        right_learning_reward_0.text = "";
                    }
                }
            }
        }
    } else {
        if ((trials0[(current_trial0 - 1)][0] === "1-2.jpg")) {
            reward_B = Number.parseInt(util.round(sample_B));
            if ((l_type === "1")) {
                com_par_time = 1;
                if ((key_resp_0.keys === "left")) {
                    left_learning_reward_0.text = `Reward: ${reward_B}`;
                } else {
                    if ((key_resp_0.keys === "right")) {
                        left_learning_reward_0.text = "";
                    }
                }
            } else {
                if ((l_type === "2")) {
                    com_par_time = 0.5;
                    if ((key_resp_0.keys === "left")) {
                        left_learning_reward_0.text = `Reward: ${reward_B}`;
                    } else {
                        if ((key_resp_0.keys === "right")) {
                            left_learning_reward_0.text = "";
                        }
                    }
                }
            }
            reward_A1 = Number.parseInt(util.round(sample_A1));
            if ((l_type === "1")) {
                com_par_time = 1;
                if ((key_resp_0.keys === "right")) {
                    right_learning_reward_0.text = `Reward: ${reward_A1}`;
                } else {
                    if ((key_resp_0.keys === "left")) {
                        right_learning_reward_0.text = "";
                    }
                }
            } else {
                if ((l_type === "2")) {
                    com_par_time = 0.5;
                    if ((key_resp_0.keys === "right")) {
                        right_learning_reward_0.text = `Reward: ${reward_A1}`;
                    } else {
                        if ((key_resp_0.keys === "left")) {
                            right_learning_reward_0.text = "";
                        }
                    }
                }
            }
        } else {
            if ((trials0[(current_trial0 - 1)][0] === "1-3.jpg")) {
                reward_A2 = Number.parseInt(util.round(sample_A2));
                if ((l_type === "1")) {
                    com_par_time = 1;
                    if ((key_resp_0.keys === "left")) {
                        left_learning_reward_0.text = `Reward: ${reward_A2}`;
                    } else {
                        if ((key_resp_0.keys === "right")) {
                            left_learning_reward_0.text = "";
                        }
                    }
                } else {
                    if ((l_type === "2")) {
                        com_par_time = 0.5;
                        if ((key_resp_0.keys === "left")) {
                            left_learning_reward_0.text = `Reward: ${reward_A2}`;
                        } else {
                            if ((key_resp_0.keys === "right")) {
                                left_learning_reward_0.text = "";
                            }
                        }
                    }
                }
                reward_C = Number.parseInt(util.round(sample_C));
                if ((l_type === "1")) {
                    com_par_time = 1;
                    if ((key_resp_0.keys === "right")) {
                        right_learning_reward_0.text = `Reward: ${reward_C}`;
                    } else {
                        if ((key_resp_0.keys === "left")) {
                            right_learning_reward_0.text = "";
                        }
                    }
                } else {
                    if ((l_type === "2")) {
                        com_par_time = 0.5;
                        if ((key_resp_0.keys === "right")) {
                            right_learning_reward_0.text = `Reward: ${reward_C}`;
                        } else {
                            if ((key_resp_0.keys === "left")) {
                                right_learning_reward_0.text = "";
                            }
                        }
                    }
                }
            } else {
                if ((trials0[(current_trial0 - 1)][0] === "1-4.jpg")) {
                    reward_C = Number.parseInt(util.round(sample_C));
                    if ((l_type === "1")) {
                        com_par_time = 1;
                        if ((key_resp_0.keys === "left")) {
                            left_learning_reward_0.text = `Reward: ${reward_C}`;
                        } else {
                            if ((key_resp_0.keys === "right")) {
                                left_learning_reward_0.text = "";
                            }
                        }
                    } else {
                        if ((l_type === "2")) {
                            com_par_time = 0.5;
                            if ((key_resp_0.keys === "left")) {
                                left_learning_reward_0.text = `Reward: ${reward_C}`;
                            } else {
                                if ((key_resp_0.keys === "right")) {
                                    left_learning_reward_0.text = "";
                                }
                            }
                        }
                    }
                    reward_A2 = Number.parseInt(util.round(sample_A2));
                    if ((l_type === "1")) {
                        com_par_time = 1;
                        if ((key_resp_0.keys === "right")) {
                            right_learning_reward_0.text = `Reward: ${reward_A2}`;
                        } else {
                            if ((key_resp_0.keys === "left")) {
                                right_learning_reward_0.text = "";
                            }
                        }
                    } else {
                        if ((l_type === "2")) {
                            com_par_time = 0.5;
                            if ((key_resp_0.keys === "right")) {
                                right_learning_reward_0.text = `Reward: ${reward_A2}`;
                            } else {
                                if ((key_resp_0.keys === "left")) {
                                    right_learning_reward_0.text = "";
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    if ((key_resp_0.keys === "left")) {
        pos_k0 = [(- 0.5), 0];
        if ((t >= (routineStartTime + 5.0))) {
            continueRoutine = false;
        }
    } else {
        if ((key_resp_0.keys === "right")) {
            pos_k0 = [0.5, 0];
            if ((t >= (routineStartTime + 5.0))) {
                continueRoutine = false;
            }
        } else {
            pos_k0 = [1.5, 0];
            if (((t >= (routineStartTime + 5.0)) && (t <= (routineStartTime + 6.0)))) {
                no_response = true;
            }
        }
    }
    
    
    if (polygon_0.status === PsychoJS.Status.STARTED){ // only update if being drawn
      polygon_0.setPos(pos_k0, false);
    }
    
    // *polygon_0* updates
    if (t >= 4 && polygon_0.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_0.tStart = t;  // (not accounting for frame time here)
      polygon_0.frameNStart = frameN;  // exact frame index
      
      polygon_0.setAutoDraw(true);
    }
    
    frameRemains = 4 + com_par_time - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (polygon_0.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygon_0.setAutoDraw(false);
    }
    
    
    // *left_learning_reward_0* updates
    if (t >= 4 && left_learning_reward_0.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      left_learning_reward_0.tStart = t;  // (not accounting for frame time here)
      left_learning_reward_0.frameNStart = frameN;  // exact frame index
      
      left_learning_reward_0.setAutoDraw(true);
    }
    
    frameRemains = 4 + com_par_time - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (left_learning_reward_0.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      left_learning_reward_0.setAutoDraw(false);
    }
    
    
    // *right_learning_reward_0* updates
    if (t >= 4 && right_learning_reward_0.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      right_learning_reward_0.tStart = t;  // (not accounting for frame time here)
      right_learning_reward_0.frameNStart = frameN;  // exact frame index
      
      right_learning_reward_0.setAutoDraw(true);
    }
    
    frameRemains = 4 + com_par_time - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (right_learning_reward_0.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      right_learning_reward_0.setAutoDraw(false);
    }
    
    
    if (text_no_resp_0.status === PsychoJS.Status.STARTED){ // only update if being drawn
      text_no_resp_0.setText('پاسخی دریافت نشد.', false);
    }
    
    // *text_no_resp_0* updates
    if ((no_response) && text_no_resp_0.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_no_resp_0.tStart = t;  // (not accounting for frame time here)
      text_no_resp_0.frameNStart = frameN;  // exact frame index
      
      text_no_resp_0.setAutoDraw(true);
    }
    
    if (text_no_resp_0.status === PsychoJS.Status.STARTED && t >= (text_no_resp_0.tStart + 1.0)) {
      text_no_resp_0.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    main_trainingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function main_trainingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'main_training' ---
    main_trainingComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('main_training.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_0.corr, level);
    }
    psychoJS.experiment.addData('key_resp_0.keys', key_resp_0.keys);
    if (typeof key_resp_0.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_0.rt', key_resp_0.rt);
        psychoJS.experiment.addData('key_resp_0.duration', key_resp_0.duration);
        }
    
    key_resp_0.stop();
    // the Routine "main_training" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function text_1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'text_1' ---
    t = 0;
    text_1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('text_1.started', globalClock.getTime());
    text1_key_resp.keys = undefined;
    text1_key_resp.rt = undefined;
    _text1_key_resp_allKeys = [];
    // keep track of which components have finished
    text_1Components = [];
    text_1Components.push(text1);
    text_1Components.push(text1_key_resp);
    
    text_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function text_1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'text_1' ---
    // get current time
    t = text_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text1* updates
    if (t >= 0.0 && text1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text1.tStart = t;  // (not accounting for frame time here)
      text1.frameNStart = frameN;  // exact frame index
      
      text1.setAutoDraw(true);
    }
    
    
    // *text1_key_resp* updates
    if (t >= 0.0 && text1_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text1_key_resp.tStart = t;  // (not accounting for frame time here)
      text1_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { text1_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { text1_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { text1_key_resp.clearEvents(); });
    }
    
    if (text1_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = text1_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _text1_key_resp_allKeys = _text1_key_resp_allKeys.concat(theseKeys);
      if (_text1_key_resp_allKeys.length > 0) {
        text1_key_resp.keys = _text1_key_resp_allKeys[_text1_key_resp_allKeys.length - 1].name;  // just the last key pressed
        text1_key_resp.rt = _text1_key_resp_allKeys[_text1_key_resp_allKeys.length - 1].rt;
        text1_key_resp.duration = _text1_key_resp_allKeys[_text1_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    text_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function text_1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'text_1' ---
    text_1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('text_1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(text1_key_resp.corr, level);
    }
    psychoJS.experiment.addData('text1_key_resp.keys', text1_key_resp.keys);
    if (typeof text1_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('text1_key_resp.rt', text1_key_resp.rt);
        psychoJS.experiment.addData('text1_key_resp.duration', text1_key_resp.duration);
        routineTimer.reset();
        }
    
    text1_key_resp.stop();
    // the Routine "text_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function fixation_learningRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixation_learning' ---
    t = 0;
    fixation_learningClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('fixation_learning.started', globalClock.getTime());
    // keep track of which components have finished
    fixation_learningComponents = [];
    fixation_learningComponents.push(fixation1);
    
    fixation_learningComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function fixation_learningRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixation_learning' ---
    // get current time
    t = fixation_learningClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation1* updates
    if (t >= 0.0 && fixation1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation1.tStart = t;  // (not accounting for frame time here)
      fixation1.frameNStart = frameN;  // exact frame index
      
      fixation1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation1.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixation_learningComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function fixation_learningRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixation_learning' ---
    fixation_learningComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('fixation_learning.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function main_learningRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'main_learning' ---
    t = 0;
    main_learningClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('main_learning.started', globalClock.getTime());
    main_learningStartWinParams = {
        'color': psychoJS.window.color,
        'colorSpace': psychoJS.window.colorSpace,
        'backgroundImage': psychoJS.window.backgroundImage,
        'backgroundFit': psychoJS.window.backgroundFit,
    };
    psychoJS.window.color = [1.0, 1.0, 1.0];
    psychoJS.window.colorSpace = 'rgb';
    psychoJS.window.backgroundImage = '';
    psychoJS.window.backgroundFit = 'none';
    // Run 'Begin Routine' code from learning_code
    leftimage = trials[current_trial][0];
    rightimage = trials[current_trial][1];
    current_trial += 1;
    
    left_image.setImage(leftimage);
    right_image.setImage(rightimage);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // Run 'Begin Routine' code from code
    sample_A1 = (- 1);
    sample_B = (- 1);
    sample_A2 = (- 1);
    sample_C = (- 1);
    while (((sample_A1 < 0) || (sample_A1 > 100))) {
        sample_A1 = np.random.normal(64, 13, 1)[0];
    }
    while (((sample_B < 0) || (sample_A1 > 100))) {
        sample_B = np.random.normal(54, 13, 1)[0];
    }
    while (((sample_A2 < 0) || (sample_A1 > 100))) {
        sample_A2 = np.random.normal(64, 13, 1)[0];
    }
    while (((sample_C < 0) || (sample_A1 > 100))) {
        sample_C = np.random.normal(44, 13, 1)[0];
    }
    no_response = false;
    routineStartTime = t;
    
    left_learning_reward.setText('');
    right_learning_reward.setText('');
    // keep track of which components have finished
    main_learningComponents = [];
    main_learningComponents.push(left_image);
    main_learningComponents.push(right_image);
    main_learningComponents.push(key_resp);
    main_learningComponents.push(polygon);
    main_learningComponents.push(left_learning_reward);
    main_learningComponents.push(right_learning_reward);
    main_learningComponents.push(text_no_resp);
    
    main_learningComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function main_learningRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'main_learning' ---
    // get current time
    t = main_learningClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *left_image* updates
    if (t >= 0 && left_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      left_image.tStart = t;  // (not accounting for frame time here)
      left_image.frameNStart = frameN;  // exact frame index
      
      left_image.setAutoDraw(true);
    }
    
    frameRemains = 0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (left_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      left_image.setAutoDraw(false);
    }
    
    
    // *right_image* updates
    if (t >= 0 && right_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      right_image.tStart = t;  // (not accounting for frame time here)
      right_image.frameNStart = frameN;  // exact frame index
      
      right_image.setAutoDraw(true);
    }
    
    frameRemains = 0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (right_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      right_image.setAutoDraw(false);
    }
    
    
    // *key_resp* updates
    if (t >= 0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    frameRemains = 0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['right', 'left'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
      }
    }
    
    // Run 'Each Frame' code from code
    if ((trials[(current_trial - 1)][0] === "1.jpg")) {
        reward_A1 = Number.parseInt(util.round(sample_A1));
        psychoJS.experiment.addData("reward_A1", reward_A1);
        if ((l_type === "1")) {
            com_par_time = 1;
            if ((key_resp.keys === "left")) {
                left_learning_reward.text = `Reward: ${reward_A1}`;
                psychoJS.experiment.addData("gain_reward", reward_A1);
                total_reward = (total_reward + reward_A1);
            } else {
                if ((key_resp.keys === "right")) {
                    left_learning_reward.text = "";
                }
            }
        } else {
            if ((l_type === "2")) {
                com_par_time = 0.5;
                if ((key_resp.keys === "left")) {
                    left_learning_reward.text = `Reward: ${reward_A1}`;
                    psychoJS.experiment.addData("gain_reward", reward_A1);
                    total_reward = (total_reward + reward_A1);
                } else {
                    if ((key_resp.keys === "right")) {
                        left_learning_reward.text = "";
                    }
                }
            }
        }
        reward_B = Number.parseInt(util.round(sample_B));
        psychoJS.experiment.addData("reward_B", reward_B);
        if ((l_type === "1")) {
            com_par_time = 1;
            if ((key_resp.keys === "right")) {
                right_learning_reward.text = `Reward: ${reward_B}`;
                psychoJS.experiment.addData("gain_reward", reward_B);
                total_reward = (total_reward + reward_B);
            } else {
                if ((key_resp.keys === "left")) {
                    right_learning_reward.text = "";
                }
            }
        } else {
            if ((l_type === "2")) {
                com_par_time = 0.5;
                if ((key_resp.keys === "right")) {
                    right_learning_reward.text = `Reward: ${reward_B}`;
                    psychoJS.experiment.addData("gain_reward", reward_B);
                    total_reward = (total_reward + reward_B);
                } else {
                    if ((key_resp.keys === "left")) {
                        right_learning_reward.text = "";
                    }
                }
            }
        }
    } else {
        if ((trials[(current_trial - 1)][0] === "2.jpg")) {
            reward_B = Number.parseInt(util.round(sample_B));
            psychoJS.experiment.addData("reward_B", reward_B);
            if ((l_type === "1")) {
                com_par_time = 1;
                if ((key_resp.keys === "left")) {
                    left_learning_reward.text = `Reward: ${reward_B}`;
                    psychoJS.experiment.addData("gain_reward", reward_B);
                    total_reward = (total_reward + reward_B);
                } else {
                    if ((key_resp.keys === "right")) {
                        left_learning_reward.text = "";
                    }
                }
            } else {
                if ((l_type === "2")) {
                    com_par_time = 0.5;
                    if ((key_resp.keys === "left")) {
                        left_learning_reward.text = `Reward: ${reward_B}`;
                        psychoJS.experiment.addData("gain_reward", reward_B);
                        total_reward = (total_reward + reward_B);
                    } else {
                        if ((key_resp.keys === "right")) {
                            left_learning_reward.text = "";
                        }
                    }
                }
            }
            reward_A1 = Number.parseInt(util.round(sample_A1));
            psychoJS.experiment.addData("reward_A1", reward_A1);
            if ((l_type === "1")) {
                com_par_time = 1;
                if ((key_resp.keys === "right")) {
                    right_learning_reward.text = `Reward: ${reward_A1}`;
                    psychoJS.experiment.addData("gain_reward", reward_A1);
                    total_reward = (total_reward + reward_A1);
                } else {
                    if ((key_resp.keys === "left")) {
                        right_learning_reward.text = "";
                    }
                }
            } else {
                if ((l_type === "2")) {
                    com_par_time = 0.5;
                    if ((key_resp.keys === "right")) {
                        right_learning_reward.text = `Reward: ${reward_A1}`;
                        psychoJS.experiment.addData("gain_reward", reward_A1);
                        total_reward = (total_reward + reward_A1);
                    } else {
                        if ((key_resp.keys === "left")) {
                            right_learning_reward.text = "";
                        }
                    }
                }
            }
        } else {
            if ((trials[(current_trial - 1)][0] === "3.jpg")) {
                reward_A2 = Number.parseInt(util.round(sample_A2));
                psychoJS.experiment.addData("reward_A2", reward_A2);
                if ((l_type === "1")) {
                    com_par_time = 1;
                    if ((key_resp.keys === "left")) {
                        left_learning_reward.text = `Reward: ${reward_A2}`;
                        psychoJS.experiment.addData("gain_reward", reward_A2);
                        total_reward = (total_reward + reward_A2);
                    } else {
                        if ((key_resp.keys === "right")) {
                            left_learning_reward.text = "";
                        }
                    }
                } else {
                    if ((l_type === "2")) {
                        com_par_time = 0.5;
                        if ((key_resp.keys === "left")) {
                            left_learning_reward.text = `Reward: ${reward_A2}`;
                            psychoJS.experiment.addData("gain_reward", reward_A2);
                            total_reward = (total_reward + reward_A2);
                        } else {
                            if ((key_resp.keys === "right")) {
                                left_learning_reward.text = "";
                            }
                        }
                    }
                }
                reward_C = Number.parseInt(util.round(sample_C));
                psychoJS.experiment.addData("reward_C", reward_C);
                if ((l_type === "1")) {
                    com_par_time = 1;
                    if ((key_resp.keys === "right")) {
                        right_learning_reward.text = `Reward: ${reward_C}`;
                        psychoJS.experiment.addData("gain_reward", reward_C);
                        total_reward = (total_reward + reward_C);
                    } else {
                        if ((key_resp.keys === "left")) {
                            right_learning_reward.text = "";
                        }
                    }
                } else {
                    if ((l_type === "2")) {
                        com_par_time = 0.5;
                        if ((key_resp.keys === "right")) {
                            right_learning_reward.text = `Reward: ${reward_C}`;
                            psychoJS.experiment.addData("gain_reward", reward_C);
                            total_reward = (total_reward + reward_C);
                        } else {
                            if ((key_resp.keys === "left")) {
                                right_learning_reward.text = "";
                            }
                        }
                    }
                }
            } else {
                if ((trials[(current_trial - 1)][0] === "4.jpg")) {
                    reward_C = Number.parseInt(util.round(sample_C));
                    psychoJS.experiment.addData("reward_C", reward_C);
                    if ((l_type === "1")) {
                        com_par_time = 1;
                        if ((key_resp.keys === "left")) {
                            left_learning_reward.text = `Reward: ${reward_C}`;
                            psychoJS.experiment.addData("gain_reward", reward_C);
                            total_reward = (total_reward + reward_C);
                        } else {
                            if ((key_resp.keys === "right")) {
                                left_learning_reward.text = "";
                            }
                        }
                    } else {
                        if ((l_type === "2")) {
                            com_par_time = 0.5;
                            if ((key_resp.keys === "left")) {
                                left_learning_reward.text = `Reward: ${reward_C}`;
                                psychoJS.experiment.addData("gain_reward", reward_C);
                                total_reward = (total_reward + reward_C);
                            } else {
                                if ((key_resp.keys === "right")) {
                                    left_learning_reward.text = "";
                                }
                            }
                        }
                    }
                    reward_A2 = Number.parseInt(util.round(sample_A2));
                    psychoJS.experiment.addData("reward_A2", reward_A2);
                    if ((l_type === "1")) {
                        com_par_time = 1;
                        if ((key_resp.keys === "right")) {
                            right_learning_reward.text = `Reward: ${reward_A2}`;
                            psychoJS.experiment.addData("gain_reward", reward_A2);
                            total_reward = (total_reward + reward_A2);
                        } else {
                            if ((key_resp.keys === "left")) {
                                right_learning_reward.text = "";
                            }
                        }
                    } else {
                        if ((l_type === "2")) {
                            com_par_time = 0.5;
                            if ((key_resp.keys === "right")) {
                                right_learning_reward.text = `Reward: ${reward_A2}`;
                                psychoJS.experiment.addData("gain_reward", reward_A2);
                                total_reward = (total_reward + reward_A2);
                            } else {
                                if ((key_resp.keys === "left")) {
                                    right_learning_reward.text = "";
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    if ((key_resp.keys === "left")) {
        pos_k = [(- 0.5), 0];
        if ((t >= (routineStartTime + 5.0))) {
            continueRoutine = false;
        }
    } else {
        if ((key_resp.keys === "right")) {
            pos_k = [0.5, 0];
            if ((t >= (routineStartTime + 5.0))) {
                continueRoutine = false;
            }
        } else {
            pos_k = [1.5, 0];
            if (((t >= (routineStartTime + 5.0)) && (t <= (routineStartTime + 6.0)))) {
                no_response = true;
            }
        }
    }
    
    
    if (polygon.status === PsychoJS.Status.STARTED){ // only update if being drawn
      polygon.setPos(pos_k, false);
    }
    
    // *polygon* updates
    if (t >= 4 && polygon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon.tStart = t;  // (not accounting for frame time here)
      polygon.frameNStart = frameN;  // exact frame index
      
      polygon.setAutoDraw(true);
    }
    
    frameRemains = 4 + com_par_time - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (polygon.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygon.setAutoDraw(false);
    }
    
    
    // *left_learning_reward* updates
    if (t >= 4 && left_learning_reward.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      left_learning_reward.tStart = t;  // (not accounting for frame time here)
      left_learning_reward.frameNStart = frameN;  // exact frame index
      
      left_learning_reward.setAutoDraw(true);
    }
    
    frameRemains = 4 + com_par_time - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (left_learning_reward.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      left_learning_reward.setAutoDraw(false);
    }
    
    
    // *right_learning_reward* updates
    if (t >= 4 && right_learning_reward.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      right_learning_reward.tStart = t;  // (not accounting for frame time here)
      right_learning_reward.frameNStart = frameN;  // exact frame index
      
      right_learning_reward.setAutoDraw(true);
    }
    
    frameRemains = 4 + com_par_time - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (right_learning_reward.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      right_learning_reward.setAutoDraw(false);
    }
    
    
    if (text_no_resp.status === PsychoJS.Status.STARTED){ // only update if being drawn
      text_no_resp.setText('پاسخی دریافت نشد.', false);
    }
    
    // *text_no_resp* updates
    if ((no_response) && text_no_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_no_resp.tStart = t;  // (not accounting for frame time here)
      text_no_resp.frameNStart = frameN;  // exact frame index
      
      text_no_resp.setAutoDraw(true);
    }
    
    if (text_no_resp.status === PsychoJS.Status.STARTED && t >= (text_no_resp.tStart + 1.0)) {
      text_no_resp.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    main_learningComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function main_learningRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'main_learning' ---
    main_learningComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('main_learning.stopped', globalClock.getTime());
    psychoJS.window.color = main_learningStartWinParams['color'];
    psychoJS.window.colorSpace = main_learningStartWinParams['colorSpace'];
    psychoJS.window.backgroundImage = main_learningStartWinParams['backgroundImage'];
    psychoJS.window.backgroundFit = main_learningStartWinParams['backgroundFit'];
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        }
    
    key_resp.stop();
    // the Routine "main_learning" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function text_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'text_2' ---
    t = 0;
    text_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('text_2.started', globalClock.getTime());
    text2_key_resp.keys = undefined;
    text2_key_resp.rt = undefined;
    _text2_key_resp_allKeys = [];
    // keep track of which components have finished
    text_2Components = [];
    text_2Components.push(text2);
    text_2Components.push(text2_key_resp);
    
    text_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function text_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'text_2' ---
    // get current time
    t = text_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text2* updates
    if (t >= 0.0 && text2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text2.tStart = t;  // (not accounting for frame time here)
      text2.frameNStart = frameN;  // exact frame index
      
      text2.setAutoDraw(true);
    }
    
    
    // *text2_key_resp* updates
    if (t >= 0.0 && text2_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text2_key_resp.tStart = t;  // (not accounting for frame time here)
      text2_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { text2_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { text2_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { text2_key_resp.clearEvents(); });
    }
    
    if (text2_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = text2_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _text2_key_resp_allKeys = _text2_key_resp_allKeys.concat(theseKeys);
      if (_text2_key_resp_allKeys.length > 0) {
        text2_key_resp.keys = _text2_key_resp_allKeys[_text2_key_resp_allKeys.length - 1].name;  // just the last key pressed
        text2_key_resp.rt = _text2_key_resp_allKeys[_text2_key_resp_allKeys.length - 1].rt;
        text2_key_resp.duration = _text2_key_resp_allKeys[_text2_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    text_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function text_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'text_2' ---
    text_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('text_2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(text2_key_resp.corr, level);
    }
    psychoJS.experiment.addData('text2_key_resp.keys', text2_key_resp.keys);
    if (typeof text2_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('text2_key_resp.rt', text2_key_resp.rt);
        psychoJS.experiment.addData('text2_key_resp.duration', text2_key_resp.duration);
        routineTimer.reset();
        }
    
    text2_key_resp.stop();
    // the Routine "text_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function fixation_transferRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixation_transfer' ---
    t = 0;
    fixation_transferClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('fixation_transfer.started', globalClock.getTime());
    // keep track of which components have finished
    fixation_transferComponents = [];
    fixation_transferComponents.push(fixation2);
    
    fixation_transferComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function fixation_transferRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixation_transfer' ---
    // get current time
    t = fixation_transferClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation2* updates
    if (t >= 0.0 && fixation2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation2.tStart = t;  // (not accounting for frame time here)
      fixation2.frameNStart = frameN;  // exact frame index
      
      fixation2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixation_transferComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function fixation_transferRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixation_transfer' ---
    fixation_transferComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('fixation_transfer.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function main_transferRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'main_transfer' ---
    t = 0;
    main_transferClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('main_transfer.started', globalClock.getTime());
    // Run 'Begin Routine' code from transfer_code
    leftimage = trials_2[current_trial_2][0];
    rightimage = trials_2[current_trial_2][1];
    current_trial_2 += 1;
    
    left_image_2.setImage(leftimage);
    right_image_2.setImage(rightimage);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // Run 'Begin Routine' code from code_2
    start_time = t;
    end_time = 1000;
    end_time_more = false;
    
    // keep track of which components have finished
    main_transferComponents = [];
    main_transferComponents.push(left_image_2);
    main_transferComponents.push(right_image_2);
    main_transferComponents.push(key_resp_2);
    main_transferComponents.push(polygon_2);
    
    main_transferComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function main_transferRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'main_transfer' ---
    // get current time
    t = main_transferClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *left_image_2* updates
    if (t >= 0 && left_image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      left_image_2.tStart = t;  // (not accounting for frame time here)
      left_image_2.frameNStart = frameN;  // exact frame index
      
      left_image_2.setAutoDraw(true);
    }
    
    if (left_image_2.status === PsychoJS.Status.STARTED && Boolean(end_time_more)) {
      left_image_2.setAutoDraw(false);
    }
    
    
    // *right_image_2* updates
    if (t >= 0 && right_image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      right_image_2.tStart = t;  // (not accounting for frame time here)
      right_image_2.frameNStart = frameN;  // exact frame index
      
      right_image_2.setAutoDraw(true);
    }
    
    if (right_image_2.status === PsychoJS.Status.STARTED && Boolean(end_time_more)) {
      right_image_2.setAutoDraw(false);
    }
    
    
    // *key_resp_2* updates
    if (t >= 0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }
    
    frameRemains = end_time  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((key_resp_2.status === PsychoJS.Status.STARTED || key_resp_2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      key_resp_2.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['right', 'left'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
      }
    }
    
    // Run 'Each Frame' code from code_2
    if ((key_resp_2.keys === "left")) {
        pos_k_2 = [(- 0.5), 0];
        end_time = t;
        core.wait(1.0);
        end_time_more = true;
    } else {
        if ((key_resp_2.keys === "right")) {
            pos_k_2 = [0.5, 0];
            end_time = t;
            core.wait(1.0);
            end_time_more = true;
        } else {
            pos_k_2 = [1.5, 0];
        }
    }
    
    
    if (polygon_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      polygon_2.setPos(pos_k_2, false);
    }
    
    // *polygon_2* updates
    if (t >= end_time && polygon_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_2.tStart = t;  // (not accounting for frame time here)
      polygon_2.frameNStart = frameN;  // exact frame index
      
      polygon_2.setAutoDraw(true);
    }
    
    frameRemains = end_time + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (polygon_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygon_2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    main_transferComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function main_transferRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'main_transfer' ---
    main_transferComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('main_transfer.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
        }
    
    key_resp_2.stop();
    // the Routine "main_transfer" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function slider_transferRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'slider_transfer' ---
    t = 0;
    slider_transferClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('slider_transfer.started', globalClock.getTime());
    slider_trns.reset()
    // setup some python lists for storing info about the mouse_trns
    // current position of the mouse:
    mouse_trns.x = [];
    mouse_trns.y = [];
    mouse_trns.leftButton = [];
    mouse_trns.midButton = [];
    mouse_trns.rightButton = [];
    mouse_trns.time = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from code_3
    psychoJS.window.mouseVisible = true;
    
    // keep track of which components have finished
    slider_transferComponents = [];
    slider_transferComponents.push(slider_trns);
    slider_transferComponents.push(mouse_trns);
    
    slider_transferComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function slider_transferRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'slider_transfer' ---
    // get current time
    t = slider_transferClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slider_trns* updates
    if (t >= 0 && slider_trns.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_trns.tStart = t;  // (not accounting for frame time here)
      slider_trns.frameNStart = frameN;  // exact frame index
      
      slider_trns.setAutoDraw(true);
    }
    
    
    // Check slider_trns for response to end Routine
    if (slider_trns.getRating() !== undefined && slider_trns.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // *mouse_trns* updates
    if (t >= 0.0 && mouse_trns.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_trns.tStart = t;  // (not accounting for frame time here)
      mouse_trns.frameNStart = frameN;  // exact frame index
      
      mouse_trns.status = PsychoJS.Status.STARTED;
      mouse_trns.mouseClock.reset();
      prevButtonState = mouse_trns.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_trns.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_trns.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse_trns.getPos();
          mouse_trns.x.push(_mouseXYs[0]);
          mouse_trns.y.push(_mouseXYs[1]);
          mouse_trns.leftButton.push(_mouseButtons[0]);
          mouse_trns.midButton.push(_mouseButtons[1]);
          mouse_trns.rightButton.push(_mouseButtons[2]);
          mouse_trns.time.push(mouse_trns.mouseClock.getTime());
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    slider_transferComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function slider_transferRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'slider_transfer' ---
    slider_transferComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('slider_transfer.stopped', globalClock.getTime());
    psychoJS.experiment.addData('slider_trns.response', slider_trns.getRating());
    psychoJS.experiment.addData('slider_trns.rt', slider_trns.getRT());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_trns.x', mouse_trns.x);
    psychoJS.experiment.addData('mouse_trns.y', mouse_trns.y);
    psychoJS.experiment.addData('mouse_trns.leftButton', mouse_trns.leftButton);
    psychoJS.experiment.addData('mouse_trns.midButton', mouse_trns.midButton);
    psychoJS.experiment.addData('mouse_trns.rightButton', mouse_trns.rightButton);
    psychoJS.experiment.addData('mouse_trns.time', mouse_trns.time);
    
    // the Routine "slider_transfer" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function text_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'text_3' ---
    t = 0;
    text_3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('text_3.started', globalClock.getTime());
    text3_key_resp.keys = undefined;
    text3_key_resp.rt = undefined;
    _text3_key_resp_allKeys = [];
    // keep track of which components have finished
    text_3Components = [];
    text_3Components.push(text3);
    text_3Components.push(text3_key_resp);
    
    text_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function text_3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'text_3' ---
    // get current time
    t = text_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text3* updates
    if (t >= 0.0 && text3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text3.tStart = t;  // (not accounting for frame time here)
      text3.frameNStart = frameN;  // exact frame index
      
      text3.setAutoDraw(true);
    }
    
    
    // *text3_key_resp* updates
    if (t >= 0.0 && text3_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text3_key_resp.tStart = t;  // (not accounting for frame time here)
      text3_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { text3_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { text3_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { text3_key_resp.clearEvents(); });
    }
    
    if (text3_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = text3_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _text3_key_resp_allKeys = _text3_key_resp_allKeys.concat(theseKeys);
      if (_text3_key_resp_allKeys.length > 0) {
        text3_key_resp.keys = _text3_key_resp_allKeys[_text3_key_resp_allKeys.length - 1].name;  // just the last key pressed
        text3_key_resp.rt = _text3_key_resp_allKeys[_text3_key_resp_allKeys.length - 1].rt;
        text3_key_resp.duration = _text3_key_resp_allKeys[_text3_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    text_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function text_3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'text_3' ---
    text_3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('text_3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(text3_key_resp.corr, level);
    }
    psychoJS.experiment.addData('text3_key_resp.keys', text3_key_resp.keys);
    if (typeof text3_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('text3_key_resp.rt', text3_key_resp.rt);
        psychoJS.experiment.addData('text3_key_resp.duration', text3_key_resp.duration);
        routineTimer.reset();
        }
    
    text3_key_resp.stop();
    // the Routine "text_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function fixation_estimationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixation_estimation' ---
    t = 0;
    fixation_estimationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('fixation_estimation.started', globalClock.getTime());
    // keep track of which components have finished
    fixation_estimationComponents = [];
    fixation_estimationComponents.push(fixation3);
    
    fixation_estimationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function fixation_estimationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixation_estimation' ---
    // get current time
    t = fixation_estimationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation3* updates
    if (t >= 0.0 && fixation3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation3.tStart = t;  // (not accounting for frame time here)
      fixation3.frameNStart = frameN;  // exact frame index
      
      fixation3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation3.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixation_estimationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function fixation_estimationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixation_estimation' ---
    fixation_estimationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('fixation_estimation.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function main_estimationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'main_estimation' ---
    t = 0;
    main_estimationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('main_estimation.started', globalClock.getTime());
    // Run 'Begin Routine' code from estimation_code
    image = trials_3[current_trial_3];
    current_trial_3 += 1;
    
    image_3.setImage(image);
    slider_estm.reset()
    // setup some python lists for storing info about the mouse_estm
    // current position of the mouse:
    mouse_estm.x = [];
    mouse_estm.y = [];
    mouse_estm.leftButton = [];
    mouse_estm.midButton = [];
    mouse_estm.rightButton = [];
    mouse_estm.time = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from code_4
    psychoJS.window.mouseVisible = true;
    
    // keep track of which components have finished
    main_estimationComponents = [];
    main_estimationComponents.push(image_3);
    main_estimationComponents.push(slider_estm);
    main_estimationComponents.push(mouse_estm);
    
    main_estimationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function main_estimationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'main_estimation' ---
    // get current time
    t = main_estimationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_3* updates
    if (t >= 0 && image_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_3.tStart = t;  // (not accounting for frame time here)
      image_3.frameNStart = frameN;  // exact frame index
      
      image_3.setAutoDraw(true);
    }
    
    
    // *slider_estm* updates
    if (t >= 0 && slider_estm.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_estm.tStart = t;  // (not accounting for frame time here)
      slider_estm.frameNStart = frameN;  // exact frame index
      
      slider_estm.setAutoDraw(true);
    }
    
    
    // Check slider_estm for response to end Routine
    if (slider_estm.getRating() !== undefined && slider_estm.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // *mouse_estm* updates
    if (t >= 0.0 && mouse_estm.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_estm.tStart = t;  // (not accounting for frame time here)
      mouse_estm.frameNStart = frameN;  // exact frame index
      
      mouse_estm.status = PsychoJS.Status.STARTED;
      mouse_estm.mouseClock.reset();
      prevButtonState = mouse_estm.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_estm.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_estm.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse_estm.getPos();
          mouse_estm.x.push(_mouseXYs[0]);
          mouse_estm.y.push(_mouseXYs[1]);
          mouse_estm.leftButton.push(_mouseButtons[0]);
          mouse_estm.midButton.push(_mouseButtons[1]);
          mouse_estm.rightButton.push(_mouseButtons[2]);
          mouse_estm.time.push(mouse_estm.mouseClock.getTime());
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    main_estimationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function main_estimationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'main_estimation' ---
    main_estimationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('main_estimation.stopped', globalClock.getTime());
    psychoJS.experiment.addData('slider_estm.response', slider_estm.getRating());
    psychoJS.experiment.addData('slider_estm.rt', slider_estm.getRT());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_estm.x', mouse_estm.x);
    psychoJS.experiment.addData('mouse_estm.y', mouse_estm.y);
    psychoJS.experiment.addData('mouse_estm.leftButton', mouse_estm.leftButton);
    psychoJS.experiment.addData('mouse_estm.midButton', mouse_estm.midButton);
    psychoJS.experiment.addData('mouse_estm.rightButton', mouse_estm.rightButton);
    psychoJS.experiment.addData('mouse_estm.time', mouse_estm.time);
    
    // the Routine "main_estimation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function show_rewardRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'show_reward' ---
    t = 0;
    show_rewardClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('show_reward.started', globalClock.getTime());
    totalRewardText.setText(`Total reward: ${total_reward}`);
    // keep track of which components have finished
    show_rewardComponents = [];
    show_rewardComponents.push(text4);
    show_rewardComponents.push(totalRewardText);
    
    show_rewardComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function show_rewardRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'show_reward' ---
    // get current time
    t = show_rewardClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text4* updates
    if (t >= 0.0 && text4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text4.tStart = t;  // (not accounting for frame time here)
      text4.frameNStart = frameN;  // exact frame index
      
      text4.setAutoDraw(true);
    }
    
    
    // *totalRewardText* updates
    if (t >= 0.0 && totalRewardText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      totalRewardText.tStart = t;  // (not accounting for frame time here)
      totalRewardText.frameNStart = frameN;  // exact frame index
      
      totalRewardText.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    show_rewardComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function show_rewardRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'show_reward' ---
    show_rewardComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('show_reward.stopped', globalClock.getTime());
    // the Routine "show_reward" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
