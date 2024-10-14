#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.4),
    on May 29, 2024, at 07:15
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.4'
expName = 'article2'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'seeker observee': '0.7',
    'averse observee': '0.3',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1280, 720]
_loggingLevel = logging.getLevel('warning')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='D:\\UT\\semester 4 - courses\\Cognitive science\\HWs\\HW1\\answer\\article2\\article2_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=True,
            monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [1.0000, 1.0000, 1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('text1_key_resp') is None:
        # initialise text1_key_resp
        text1_key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='text1_key_resp',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('text4_key_resp') is None:
        # initialise text4_key_resp
        text4_key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='text4_key_resp',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('text2_key_resp') is None:
        # initialise text2_key_resp
        text2_key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='text2_key_resp',
        )
    if deviceManager.getDevice('text3_key_resp') is None:
        # initialise text3_key_resp
        text3_key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='text3_key_resp',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "text_1" ---
    text1 = visual.TextStim(win=win, name='text1',
        text='در ادامه تعدادی شرط بندی با احتمال برنده شدن در هر یک\nنمایش داده شده است. می\u200cتوانید در آن شرکت کنید یا نکنید.\nدر صورتی که در آن شرکت نکنید،\n۱۰ دلار تضمین شده برنده می\u200cشوید.\n\nبرای اعلام پذیرش یا عدم پذیرش شرکت در شرط بندی\nاز میان دو گزینه\u200cی Accept و Reject\nبا فشردن کلیدهای چپ و راست، یکی را انتخاب کنید.\n\n(در صورت آماده بودن، کلید space فشار دهید.)',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    text1_key_resp = keyboard.Keyboard(deviceName='text1_key_resp')
    
    # --- Initialize components for Routine "intertrial" ---
    fixation1 = visual.ShapeStim(
        win=win, name='fixation1', vertices='cross',units='norm', 
        size=(0.03, 0.06),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=0.08,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor='black',
        opacity=None, depth=0.0, interpolate=True)
    # Run 'Begin Experiment' code from code
    import random
    
    
    # --- Initialize components for Routine "self_trial" ---
    image1 = visual.ImageStim(
        win=win,
        name='image1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.2), size=(1, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    # Run 'Begin Experiment' code from code_3
    reject = 'Reject'
    accept = 'Accept'
    
    pos_k =(0,0)
    
    textbox_left = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         pos=(-0.2, -0.2),     letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_left',
         depth=-3, autoLog=True,
    )
    textbox_right = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         pos=(0.2, -0.2),     letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_right',
         depth=-4, autoLog=True,
    )
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    polygon = visual.Rect(
        win=win, name='polygon',
        width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=20.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, -1.0000], fillColor=[0.0000, 0.0000, 0.0000],
        opacity=0.3, depth=-6.0, interpolate=True)
    
    # --- Initialize components for Routine "text_3" ---
    text4 = visual.TextStim(win=win, name='text4',
        text='در ادامه تعدادی شرط بندی و احتمال برنده شدن در هر یک\nنمایش داده شده است.\n\nبرای پیشبینی پذیرش یا عدم پذیرش شرکت در شرط بندی\nتوسط شرکت کننده\u200cی دیگر\nاز میان دو گزینه\u200cی Accept و Reject\nبا فشردن کلیدهای چپ و راست، یکی را انتخاب کنید.\n\n(در صورت آماده بودن، کلید space فشار دهید.)',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    text4_key_resp = keyboard.Keyboard(deviceName='text4_key_resp')
    
    # --- Initialize components for Routine "intertrial" ---
    fixation1 = visual.ShapeStim(
        win=win, name='fixation1', vertices='cross',units='norm', 
        size=(0.03, 0.06),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=0.08,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor='black',
        opacity=None, depth=0.0, interpolate=True)
    # Run 'Begin Experiment' code from code
    import random
    
    
    # --- Initialize components for Routine "predict_trial" ---
    image3 = visual.ImageStim(
        win=win,
        name='image3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.2), size=(1, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    # Run 'Begin Experiment' code from code_7
    reject = 'Reject'
    accept = 'Accept'
    
    pos_k =(0,0)
    
    textbox_left_3 = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         pos=(-0.2, -0.2),     letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_left_3',
         depth=-3, autoLog=True,
    )
    textbox_right_3 = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         pos=(0.2, -0.2),     letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_right_3',
         depth=-4, autoLog=True,
    )
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    polygon_3 = visual.Rect(
        win=win, name='polygon_3',
        width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=20.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, -1.0000], fillColor=[0.0000, 0.0000, 0.0000],
        opacity=0.3, depth=-6.0, interpolate=True)
    
    # --- Initialize components for Routine "text_2" ---
    text2 = visual.TextStim(win=win, name='text2',
        text='در ادامه تعدادی شرط بندی با احتمال برنده شدن\nو همچنین گزینه\u200cی انتخاب شده توسط یک شرکت کننده\u200cی\nدیگر نمایش داده شده است. \n\nبه این انتخاب\u200cها توجه کنید.\n\n(در صورت آماده بودن، کلید space فشار دهید.)',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    text2_key_resp = keyboard.Keyboard(deviceName='text2_key_resp')
    
    # --- Initialize components for Routine "intertrial" ---
    fixation1 = visual.ShapeStim(
        win=win, name='fixation1', vertices='cross',units='norm', 
        size=(0.03, 0.06),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=0.08,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor='black',
        opacity=None, depth=0.0, interpolate=True)
    # Run 'Begin Experiment' code from code
    import random
    
    
    # --- Initialize components for Routine "observe_trial_averse" ---
    image2 = visual.ImageStim(
        win=win,
        name='image2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.2), size=(1, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    # Run 'Begin Experiment' code from code_5
    import numpy as np
    import math
    
    
    reject = 'Reject'
    accept = 'Accept'
    
    pos_k =(0,0)
    
    
    
    
    aver = expInfo['averse observee']
    
    
    
    
    utility =  float(aver) - 0.5
    
    accept_num = int(2 * float(aver))
    reject_num = 2 - accept_num
    
    
    
    # Create an array with accept_num 1's and reject_num 0's
    accept_reject = np.array([1] * accept_num + [0] * reject_num)
    random.shuffle(accept_reject)
    
    
    accept_reject_i = 0
    textbox_left_2 = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         pos=(-0.2, -0.2),     letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_left_2',
         depth=-3, autoLog=True,
    )
    textbox_right_2 = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         pos=(0.2, -0.2),     letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_right_2',
         depth=-4, autoLog=True,
    )
    polygon_2 = visual.Rect(
        win=win, name='polygon_2',
        width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=20.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, -1.0000], fillColor=[0.0000, 0.0000, 0.0000],
        opacity=0.3, depth=-5.0, interpolate=True)
    
    # --- Initialize components for Routine "third_click" ---
    text3 = visual.TextStim(win=win, name='text3',
        text='لطفا کلید space فشار دهید.',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    text3_key_resp = keyboard.Keyboard(deviceName='text3_key_resp')
    
    # --- Initialize components for Routine "text_1" ---
    text1 = visual.TextStim(win=win, name='text1',
        text='در ادامه تعدادی شرط بندی با احتمال برنده شدن در هر یک\nنمایش داده شده است. می\u200cتوانید در آن شرکت کنید یا نکنید.\nدر صورتی که در آن شرکت نکنید،\n۱۰ دلار تضمین شده برنده می\u200cشوید.\n\nبرای اعلام پذیرش یا عدم پذیرش شرکت در شرط بندی\nاز میان دو گزینه\u200cی Accept و Reject\nبا فشردن کلیدهای چپ و راست، یکی را انتخاب کنید.\n\n(در صورت آماده بودن، کلید space فشار دهید.)',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    text1_key_resp = keyboard.Keyboard(deviceName='text1_key_resp')
    
    # --- Initialize components for Routine "intertrial" ---
    fixation1 = visual.ShapeStim(
        win=win, name='fixation1', vertices='cross',units='norm', 
        size=(0.03, 0.06),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=0.08,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor='black',
        opacity=None, depth=0.0, interpolate=True)
    # Run 'Begin Experiment' code from code
    import random
    
    
    # --- Initialize components for Routine "self_trial" ---
    image1 = visual.ImageStim(
        win=win,
        name='image1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.2), size=(1, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    # Run 'Begin Experiment' code from code_3
    reject = 'Reject'
    accept = 'Accept'
    
    pos_k =(0,0)
    
    textbox_left = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         pos=(-0.2, -0.2),     letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_left',
         depth=-3, autoLog=True,
    )
    textbox_right = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         pos=(0.2, -0.2),     letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_right',
         depth=-4, autoLog=True,
    )
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    polygon = visual.Rect(
        win=win, name='polygon',
        width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=20.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, -1.0000], fillColor=[0.0000, 0.0000, 0.0000],
        opacity=0.3, depth=-6.0, interpolate=True)
    
    # --- Initialize components for Routine "text_3" ---
    text4 = visual.TextStim(win=win, name='text4',
        text='در ادامه تعدادی شرط بندی و احتمال برنده شدن در هر یک\nنمایش داده شده است.\n\nبرای پیشبینی پذیرش یا عدم پذیرش شرکت در شرط بندی\nتوسط شرکت کننده\u200cی دیگر\nاز میان دو گزینه\u200cی Accept و Reject\nبا فشردن کلیدهای چپ و راست، یکی را انتخاب کنید.\n\n(در صورت آماده بودن، کلید space فشار دهید.)',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    text4_key_resp = keyboard.Keyboard(deviceName='text4_key_resp')
    
    # --- Initialize components for Routine "intertrial" ---
    fixation1 = visual.ShapeStim(
        win=win, name='fixation1', vertices='cross',units='norm', 
        size=(0.03, 0.06),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=0.08,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor='black',
        opacity=None, depth=0.0, interpolate=True)
    # Run 'Begin Experiment' code from code
    import random
    
    
    # --- Initialize components for Routine "predict_trial" ---
    image3 = visual.ImageStim(
        win=win,
        name='image3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.2), size=(1, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    # Run 'Begin Experiment' code from code_7
    reject = 'Reject'
    accept = 'Accept'
    
    pos_k =(0,0)
    
    textbox_left_3 = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         pos=(-0.2, -0.2),     letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_left_3',
         depth=-3, autoLog=True,
    )
    textbox_right_3 = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         pos=(0.2, -0.2),     letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_right_3',
         depth=-4, autoLog=True,
    )
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    polygon_3 = visual.Rect(
        win=win, name='polygon_3',
        width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=20.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, -1.0000], fillColor=[0.0000, 0.0000, 0.0000],
        opacity=0.3, depth=-6.0, interpolate=True)
    
    # --- Initialize components for Routine "text_2" ---
    text2 = visual.TextStim(win=win, name='text2',
        text='در ادامه تعدادی شرط بندی با احتمال برنده شدن\nو همچنین گزینه\u200cی انتخاب شده توسط یک شرکت کننده\u200cی\nدیگر نمایش داده شده است. \n\nبه این انتخاب\u200cها توجه کنید.\n\n(در صورت آماده بودن، کلید space فشار دهید.)',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    text2_key_resp = keyboard.Keyboard(deviceName='text2_key_resp')
    
    # --- Initialize components for Routine "intertrial" ---
    fixation1 = visual.ShapeStim(
        win=win, name='fixation1', vertices='cross',units='norm', 
        size=(0.03, 0.06),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=0.08,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor='black',
        opacity=None, depth=0.0, interpolate=True)
    # Run 'Begin Experiment' code from code
    import random
    
    
    # --- Initialize components for Routine "observe_trial_seek" ---
    image4 = visual.ImageStim(
        win=win,
        name='image4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.2), size=(1, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    # Run 'Begin Experiment' code from code_9
    import numpy as np
    import math
    
    
    reject = 'Reject'
    accept = 'Accept'
    
    pos_k =(0,0)
    
    
    
    
    seek = expInfo['seeker observee']
    
    utility_2 =  float(seek) - 0.5
    accept_num_2 = int(2 * float(seek))
    reject_num_2 = 2 - accept_num_2
    
    
    # Create an array with accept_num 1's and reject_num 0's
    accept_reject_2 = np.array([1] * accept_num_2 + [0] * reject_num_2)
    random.shuffle(accept_reject_2)
    
    
    accept_reject_i_2 = 0
    textbox_left_4 = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         pos=(-0.2, -0.2),     letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_left_4',
         depth=-3, autoLog=True,
    )
    textbox_right_4 = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         pos=(0.2, -0.2),     letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_right_4',
         depth=-4, autoLog=True,
    )
    polygon_4 = visual.Rect(
        win=win, name='polygon_4',
        width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=20.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, -1.0000], fillColor=[0.0000, 0.0000, 0.0000],
        opacity=0.3, depth=-5.0, interpolate=True)
    
    # --- Initialize components for Routine "third_click" ---
    text3 = visual.TextStim(win=win, name='text3',
        text='لطفا کلید space فشار دهید.',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    text3_key_resp = keyboard.Keyboard(deviceName='text3_key_resp')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "text_1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('text_1.started', globalClock.getTime(format='float'))
    text1_key_resp.keys = []
    text1_key_resp.rt = []
    _text1_key_resp_allKeys = []
    # keep track of which components have finished
    text_1Components = [text1, text1_key_resp]
    for thisComponent in text_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "text_1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text1* updates
        
        # if text1 is starting this frame...
        if text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text1.frameNStart = frameN  # exact frame index
            text1.tStart = t  # local t and not account for scr refresh
            text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text1.started')
            # update status
            text1.status = STARTED
            text1.setAutoDraw(True)
        
        # if text1 is active this frame...
        if text1.status == STARTED:
            # update params
            pass
        
        # *text1_key_resp* updates
        waitOnFlip = False
        
        # if text1_key_resp is starting this frame...
        if text1_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text1_key_resp.frameNStart = frameN  # exact frame index
            text1_key_resp.tStart = t  # local t and not account for scr refresh
            text1_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text1_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text1_key_resp.started')
            # update status
            text1_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(text1_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(text1_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if text1_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = text1_key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _text1_key_resp_allKeys.extend(theseKeys)
            if len(_text1_key_resp_allKeys):
                text1_key_resp.keys = _text1_key_resp_allKeys[-1].name  # just the last key pressed
                text1_key_resp.rt = _text1_key_resp_allKeys[-1].rt
                text1_key_resp.duration = _text1_key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in text_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "text_1" ---
    for thisComponent in text_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('text_1.stopped', globalClock.getTime(format='float'))
    # check responses
    if text1_key_resp.keys in ['', [], None]:  # No response was made
        text1_key_resp.keys = None
    thisExp.addData('text1_key_resp.keys',text1_key_resp.keys)
    if text1_key_resp.keys != None:  # we had a response
        thisExp.addData('text1_key_resp.rt', text1_key_resp.rt)
        thisExp.addData('text1_key_resp.duration', text1_key_resp.duration)
    thisExp.nextEntry()
    # the Routine "text_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    selt_trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('award-probability.xlsx', selection='0:3'),
        seed=None, name='selt_trials')
    thisExp.addLoop(selt_trials)  # add the loop to the experiment
    thisSelt_trial = selt_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSelt_trial.rgb)
    if thisSelt_trial != None:
        for paramName in thisSelt_trial:
            globals()[paramName] = thisSelt_trial[paramName]
    
    for thisSelt_trial in selt_trials:
        currentLoop = selt_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisSelt_trial.rgb)
        if thisSelt_trial != None:
            for paramName in thisSelt_trial:
                globals()[paramName] = thisSelt_trial[paramName]
        
        # --- Prepare to start Routine "intertrial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('intertrial.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code
        # Generate a uniform random number between 2 and 6
        inter_time = random.randint(2, 6)
        
        # keep track of which components have finished
        intertrialComponents = [fixation1]
        for thisComponent in intertrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "intertrial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation1* updates
            
            # if fixation1 is starting this frame...
            if fixation1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation1.frameNStart = frameN  # exact frame index
                fixation1.tStart = t  # local t and not account for scr refresh
                fixation1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation1.started')
                # update status
                fixation1.status = STARTED
                fixation1.setAutoDraw(True)
            
            # if fixation1 is active this frame...
            if fixation1.status == STARTED:
                # update params
                pass
            
            # if fixation1 is stopping this frame...
            if fixation1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation1.tStartRefresh + inter_time-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation1.tStop = t  # not accounting for scr refresh
                    fixation1.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation1.stopped')
                    # update status
                    fixation1.status = FINISHED
                    fixation1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in intertrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "intertrial" ---
        for thisComponent in intertrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('intertrial.stopped', globalClock.getTime(format='float'))
        # the Routine "intertrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "self_trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('self_trial.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_3
        left_right = random.randint(0, 1)
        
        
        textbox_left.reset()
        textbox_left.setText('')
        textbox_right.reset()
        textbox_right.setText('')
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        self_trialComponents = [image1, textbox_left, textbox_right, key_resp, polygon]
        for thisComponent in self_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "self_trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image1* updates
            
            # if image1 is starting this frame...
            if image1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image1.frameNStart = frameN  # exact frame index
                image1.tStart = t  # local t and not account for scr refresh
                image1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image1.started')
                # update status
                image1.status = STARTED
                image1.setAutoDraw(True)
            
            # if image1 is active this frame...
            if image1.status == STARTED:
                # update params
                image1.setImage(image_name, log=False)
            
            # if image1 is stopping this frame...
            if image1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image1.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    image1.tStop = t  # not accounting for scr refresh
                    image1.tStopRefresh = tThisFlipGlobal  # on global time
                    image1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image1.stopped')
                    # update status
                    image1.status = FINISHED
                    image1.setAutoDraw(False)
            # Run 'Each Frame' code from code_3
            if left_right == 1:
                textbox_left.text = f'{reject}'
                textbox_right.text = f'{accept}'
            elif left_right == 0:
                textbox_left.text = f'{accept}'
                textbox_right.text = f'{reject}'
            
            
            
            # Check if a key has been pressed
            if key_resp.keys == 'left':
                pos_k=[-0.2,-0.2]
            elif key_resp.keys == 'right':  # If any key other than 'right' is pressed
                pos_k=[0.2,-0.2]
            else:  # If any key other than 'right' is pressed
                pos_k=[1.5,0]
            
            
            
            # *textbox_left* updates
            
            # if textbox_left is starting this frame...
            if textbox_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_left.frameNStart = frameN  # exact frame index
                textbox_left.tStart = t  # local t and not account for scr refresh
                textbox_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_left, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_left.started')
                # update status
                textbox_left.status = STARTED
                textbox_left.setAutoDraw(True)
            
            # if textbox_left is active this frame...
            if textbox_left.status == STARTED:
                # update params
                pass
            
            # if textbox_left is stopping this frame...
            if textbox_left.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textbox_left.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    textbox_left.tStop = t  # not accounting for scr refresh
                    textbox_left.tStopRefresh = tThisFlipGlobal  # on global time
                    textbox_left.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox_left.stopped')
                    # update status
                    textbox_left.status = FINISHED
                    textbox_left.setAutoDraw(False)
            
            # *textbox_right* updates
            
            # if textbox_right is starting this frame...
            if textbox_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_right.frameNStart = frameN  # exact frame index
                textbox_right.tStart = t  # local t and not account for scr refresh
                textbox_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_right, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_right.started')
                # update status
                textbox_right.status = STARTED
                textbox_right.setAutoDraw(True)
            
            # if textbox_right is active this frame...
            if textbox_right.status == STARTED:
                # update params
                pass
            
            # if textbox_right is stopping this frame...
            if textbox_right.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textbox_right.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    textbox_right.tStop = t  # not accounting for scr refresh
                    textbox_right.tStopRefresh = tThisFlipGlobal  # on global time
                    textbox_right.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox_right.stopped')
                    # update status
                    textbox_right.status = FINISHED
                    textbox_right.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp is stopping this frame...
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.tStopRefresh = tThisFlipGlobal  # on global time
                    key_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp.stopped')
                    # update status
                    key_resp.status = FINISHED
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['right','left'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
            
            # *polygon* updates
            
            # if polygon is starting this frame...
            if polygon.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon.started')
                # update status
                polygon.status = STARTED
                polygon.setAutoDraw(True)
            
            # if polygon is active this frame...
            if polygon.status == STARTED:
                # update params
                polygon.setPos(pos_k, log=False)
            
            # if polygon is stopping this frame...
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.stopped')
                    # update status
                    polygon.status = FINISHED
                    polygon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in self_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "self_trial" ---
        for thisComponent in self_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('self_trial.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_2
        thisExp.addData('image_name', image_name)
        # Run 'End Routine' code from code_3
        if left_right == 1:
            thisExp.addData('textbox_left', 'Reject')
            thisExp.addData('textbox_right', 'Accept')
            if key_resp.keys == 'left':
                thisExp.addData('selection', 'Reject')
            elif key_resp.keys == 'right':  # If any key other than 'right' is pressed
                thisExp.addData('selection', 'Accept')
            else:  # If any key other than 'right' is pressed
                thisExp.addData('selection', '')
        elif left_right == 0:
            thisExp.addData('textbox_left', 'Accept')
            thisExp.addData('textbox_right', 'Reject')
            if key_resp.keys == 'left':
                thisExp.addData('selection', 'Accept')
            elif key_resp.keys == 'right':  # If any key other than 'right' is pressed
                thisExp.addData('selection', 'Reject')
            else:  # If any key other than 'right' is pressed
                thisExp.addData('selection', '')
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        selt_trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            selt_trials.addData('key_resp.rt', key_resp.rt)
            selt_trials.addData('key_resp.duration', key_resp.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'selt_trials'
    
    
    # --- Prepare to start Routine "text_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('text_3.started', globalClock.getTime(format='float'))
    text4_key_resp.keys = []
    text4_key_resp.rt = []
    _text4_key_resp_allKeys = []
    # keep track of which components have finished
    text_3Components = [text4, text4_key_resp]
    for thisComponent in text_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "text_3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text4* updates
        
        # if text4 is starting this frame...
        if text4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text4.frameNStart = frameN  # exact frame index
            text4.tStart = t  # local t and not account for scr refresh
            text4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text4.started')
            # update status
            text4.status = STARTED
            text4.setAutoDraw(True)
        
        # if text4 is active this frame...
        if text4.status == STARTED:
            # update params
            pass
        
        # *text4_key_resp* updates
        waitOnFlip = False
        
        # if text4_key_resp is starting this frame...
        if text4_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text4_key_resp.frameNStart = frameN  # exact frame index
            text4_key_resp.tStart = t  # local t and not account for scr refresh
            text4_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text4_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text4_key_resp.started')
            # update status
            text4_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(text4_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(text4_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if text4_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = text4_key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _text4_key_resp_allKeys.extend(theseKeys)
            if len(_text4_key_resp_allKeys):
                text4_key_resp.keys = _text4_key_resp_allKeys[-1].name  # just the last key pressed
                text4_key_resp.rt = _text4_key_resp_allKeys[-1].rt
                text4_key_resp.duration = _text4_key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in text_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "text_3" ---
    for thisComponent in text_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('text_3.stopped', globalClock.getTime(format='float'))
    # check responses
    if text4_key_resp.keys in ['', [], None]:  # No response was made
        text4_key_resp.keys = None
    thisExp.addData('text4_key_resp.keys',text4_key_resp.keys)
    if text4_key_resp.keys != None:  # we had a response
        thisExp.addData('text4_key_resp.rt', text4_key_resp.rt)
        thisExp.addData('text4_key_resp.duration', text4_key_resp.duration)
    thisExp.nextEntry()
    # the Routine "text_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    predict_trials_1 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('award-probability.xlsx', selection='1:3'),
        seed=None, name='predict_trials_1')
    thisExp.addLoop(predict_trials_1)  # add the loop to the experiment
    thisPredict_trial_1 = predict_trials_1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPredict_trial_1.rgb)
    if thisPredict_trial_1 != None:
        for paramName in thisPredict_trial_1:
            globals()[paramName] = thisPredict_trial_1[paramName]
    
    for thisPredict_trial_1 in predict_trials_1:
        currentLoop = predict_trials_1
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisPredict_trial_1.rgb)
        if thisPredict_trial_1 != None:
            for paramName in thisPredict_trial_1:
                globals()[paramName] = thisPredict_trial_1[paramName]
        
        # --- Prepare to start Routine "intertrial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('intertrial.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code
        # Generate a uniform random number between 2 and 6
        inter_time = random.randint(2, 6)
        
        # keep track of which components have finished
        intertrialComponents = [fixation1]
        for thisComponent in intertrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "intertrial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation1* updates
            
            # if fixation1 is starting this frame...
            if fixation1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation1.frameNStart = frameN  # exact frame index
                fixation1.tStart = t  # local t and not account for scr refresh
                fixation1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation1.started')
                # update status
                fixation1.status = STARTED
                fixation1.setAutoDraw(True)
            
            # if fixation1 is active this frame...
            if fixation1.status == STARTED:
                # update params
                pass
            
            # if fixation1 is stopping this frame...
            if fixation1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation1.tStartRefresh + inter_time-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation1.tStop = t  # not accounting for scr refresh
                    fixation1.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation1.stopped')
                    # update status
                    fixation1.status = FINISHED
                    fixation1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in intertrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "intertrial" ---
        for thisComponent in intertrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('intertrial.stopped', globalClock.getTime(format='float'))
        # the Routine "intertrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "predict_trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('predict_trial.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_7
        left_right = random.randint(0, 1)
        
        
        textbox_left_3.reset()
        textbox_left_3.setText('')
        textbox_right_3.reset()
        textbox_right_3.setText('')
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        predict_trialComponents = [image3, textbox_left_3, textbox_right_3, key_resp_2, polygon_3]
        for thisComponent in predict_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "predict_trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image3* updates
            
            # if image3 is starting this frame...
            if image3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image3.frameNStart = frameN  # exact frame index
                image3.tStart = t  # local t and not account for scr refresh
                image3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image3.started')
                # update status
                image3.status = STARTED
                image3.setAutoDraw(True)
            
            # if image3 is active this frame...
            if image3.status == STARTED:
                # update params
                image3.setImage(image_name, log=False)
            
            # if image3 is stopping this frame...
            if image3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image3.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    image3.tStop = t  # not accounting for scr refresh
                    image3.tStopRefresh = tThisFlipGlobal  # on global time
                    image3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image3.stopped')
                    # update status
                    image3.status = FINISHED
                    image3.setAutoDraw(False)
            # Run 'Each Frame' code from code_7
            if left_right == 1:
                textbox_left_3.text = f'{reject}'
                textbox_right_3.text = f'{accept}'
            elif left_right == 0:
                textbox_left_3.text = f'{accept}'
                textbox_right_3.text = f'{reject}'
            
            
            
            # Check if a key has been pressed
            if key_resp_2.keys == 'left':
                pos_k=[-0.2,-0.2]
            elif key_resp_2.keys == 'right':  # If any key other than 'right' is pressed
                pos_k=[0.2,-0.2]
            else:  # If any key other than 'right' is pressed
                pos_k=[1.5,0]
            
            
            
            # *textbox_left_3* updates
            
            # if textbox_left_3 is starting this frame...
            if textbox_left_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_left_3.frameNStart = frameN  # exact frame index
                textbox_left_3.tStart = t  # local t and not account for scr refresh
                textbox_left_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_left_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_left_3.started')
                # update status
                textbox_left_3.status = STARTED
                textbox_left_3.setAutoDraw(True)
            
            # if textbox_left_3 is active this frame...
            if textbox_left_3.status == STARTED:
                # update params
                pass
            
            # if textbox_left_3 is stopping this frame...
            if textbox_left_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textbox_left_3.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    textbox_left_3.tStop = t  # not accounting for scr refresh
                    textbox_left_3.tStopRefresh = tThisFlipGlobal  # on global time
                    textbox_left_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox_left_3.stopped')
                    # update status
                    textbox_left_3.status = FINISHED
                    textbox_left_3.setAutoDraw(False)
            
            # *textbox_right_3* updates
            
            # if textbox_right_3 is starting this frame...
            if textbox_right_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_right_3.frameNStart = frameN  # exact frame index
                textbox_right_3.tStart = t  # local t and not account for scr refresh
                textbox_right_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_right_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_right_3.started')
                # update status
                textbox_right_3.status = STARTED
                textbox_right_3.setAutoDraw(True)
            
            # if textbox_right_3 is active this frame...
            if textbox_right_3.status == STARTED:
                # update params
                pass
            
            # if textbox_right_3 is stopping this frame...
            if textbox_right_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textbox_right_3.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    textbox_right_3.tStop = t  # not accounting for scr refresh
                    textbox_right_3.tStopRefresh = tThisFlipGlobal  # on global time
                    textbox_right_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox_right_3.stopped')
                    # update status
                    textbox_right_3.status = FINISHED
                    textbox_right_3.setAutoDraw(False)
            
            # *key_resp_2* updates
            waitOnFlip = False
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2.started')
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_2 is stopping this frame...
            if key_resp_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_2.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_2.tStop = t  # not accounting for scr refresh
                    key_resp_2.tStopRefresh = tThisFlipGlobal  # on global time
                    key_resp_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_2.stopped')
                    # update status
                    key_resp_2.status = FINISHED
                    key_resp_2.status = FINISHED
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['right','left'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    key_resp_2.duration = _key_resp_2_allKeys[-1].duration
            
            # *polygon_3* updates
            
            # if polygon_3 is starting this frame...
            if polygon_3.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                polygon_3.frameNStart = frameN  # exact frame index
                polygon_3.tStart = t  # local t and not account for scr refresh
                polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_3.started')
                # update status
                polygon_3.status = STARTED
                polygon_3.setAutoDraw(True)
            
            # if polygon_3 is active this frame...
            if polygon_3.status == STARTED:
                # update params
                polygon_3.setPos(pos_k, log=False)
            
            # if polygon_3 is stopping this frame...
            if polygon_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_3.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_3.tStop = t  # not accounting for scr refresh
                    polygon_3.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_3.stopped')
                    # update status
                    polygon_3.status = FINISHED
                    polygon_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in predict_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "predict_trial" ---
        for thisComponent in predict_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('predict_trial.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_6
        thisExp.addData('image_name_pred', image_name)
        # Run 'End Routine' code from code_7
        if left_right == 1:
            thisExp.addData('textbox_left_pred', 'Reject')
            thisExp.addData('textbox_right_pred', 'Accept')
            if key_resp_2.keys == 'left':
                thisExp.addData('selection_pred', 'Reject')
            elif key_resp_2.keys == 'right':  # If any key other than 'right' is pressed
                thisExp.addData('selection_pred', 'Accept')
            else:  # If any key other than 'right' is pressed
                thisExp.addData('selection', '')
        elif left_right == 0:
            thisExp.addData('textbox_left_pred', 'Accept')
            thisExp.addData('textbox_right_pred', 'Reject')
            if key_resp_2.keys == 'left':
                thisExp.addData('selection_pred', 'Accept')
            elif key_resp_2.keys == 'right':  # If any key other than 'right' is pressed
                thisExp.addData('selection_pred', 'Reject')
            else:  # If any key other than 'right' is pressed
                thisExp.addData('selection_pred', '')
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        predict_trials_1.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            predict_trials_1.addData('key_resp_2.rt', key_resp_2.rt)
            predict_trials_1.addData('key_resp_2.duration', key_resp_2.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'predict_trials_1'
    
    
    # --- Prepare to start Routine "text_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('text_2.started', globalClock.getTime(format='float'))
    text2_key_resp.keys = []
    text2_key_resp.rt = []
    _text2_key_resp_allKeys = []
    # keep track of which components have finished
    text_2Components = [text2, text2_key_resp]
    for thisComponent in text_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "text_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text2* updates
        
        # if text2 is starting this frame...
        if text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text2.frameNStart = frameN  # exact frame index
            text2.tStart = t  # local t and not account for scr refresh
            text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text2.started')
            # update status
            text2.status = STARTED
            text2.setAutoDraw(True)
        
        # if text2 is active this frame...
        if text2.status == STARTED:
            # update params
            pass
        
        # *text2_key_resp* updates
        waitOnFlip = False
        
        # if text2_key_resp is starting this frame...
        if text2_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text2_key_resp.frameNStart = frameN  # exact frame index
            text2_key_resp.tStart = t  # local t and not account for scr refresh
            text2_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text2_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text2_key_resp.started')
            # update status
            text2_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(text2_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(text2_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if text2_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = text2_key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _text2_key_resp_allKeys.extend(theseKeys)
            if len(_text2_key_resp_allKeys):
                text2_key_resp.keys = _text2_key_resp_allKeys[-1].name  # just the last key pressed
                text2_key_resp.rt = _text2_key_resp_allKeys[-1].rt
                text2_key_resp.duration = _text2_key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in text_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "text_2" ---
    for thisComponent in text_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('text_2.stopped', globalClock.getTime(format='float'))
    # check responses
    if text2_key_resp.keys in ['', [], None]:  # No response was made
        text2_key_resp.keys = None
    thisExp.addData('text2_key_resp.keys',text2_key_resp.keys)
    if text2_key_resp.keys != None:  # we had a response
        thisExp.addData('text2_key_resp.rt', text2_key_resp.rt)
        thisExp.addData('text2_key_resp.duration', text2_key_resp.duration)
    thisExp.nextEntry()
    # the Routine "text_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    observe_trials_averse = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('award-probability.xlsx', selection='1:3'),
        seed=None, name='observe_trials_averse')
    thisExp.addLoop(observe_trials_averse)  # add the loop to the experiment
    thisObserve_trials_averse = observe_trials_averse.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisObserve_trials_averse.rgb)
    if thisObserve_trials_averse != None:
        for paramName in thisObserve_trials_averse:
            globals()[paramName] = thisObserve_trials_averse[paramName]
    
    for thisObserve_trials_averse in observe_trials_averse:
        currentLoop = observe_trials_averse
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisObserve_trials_averse.rgb)
        if thisObserve_trials_averse != None:
            for paramName in thisObserve_trials_averse:
                globals()[paramName] = thisObserve_trials_averse[paramName]
        
        # --- Prepare to start Routine "intertrial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('intertrial.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code
        # Generate a uniform random number between 2 and 6
        inter_time = random.randint(2, 6)
        
        # keep track of which components have finished
        intertrialComponents = [fixation1]
        for thisComponent in intertrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "intertrial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation1* updates
            
            # if fixation1 is starting this frame...
            if fixation1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation1.frameNStart = frameN  # exact frame index
                fixation1.tStart = t  # local t and not account for scr refresh
                fixation1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation1.started')
                # update status
                fixation1.status = STARTED
                fixation1.setAutoDraw(True)
            
            # if fixation1 is active this frame...
            if fixation1.status == STARTED:
                # update params
                pass
            
            # if fixation1 is stopping this frame...
            if fixation1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation1.tStartRefresh + inter_time-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation1.tStop = t  # not accounting for scr refresh
                    fixation1.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation1.stopped')
                    # update status
                    fixation1.status = FINISHED
                    fixation1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in intertrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "intertrial" ---
        for thisComponent in intertrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('intertrial.stopped', globalClock.getTime(format='float'))
        # the Routine "intertrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "observe_trial_averse" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('observe_trial_averse.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_5
        left_right = random.randint(0, 1)
        
        
        #
        #if accept_reject[accept_reject_i] == 1: # accept
        #    if left_right == 1:
        ##        textbox_left.text = f'{reject}'
        ##        textbox_right.text = f'{accept}'
        #        pos_k=[0.2,-0.2]
        #    elif left_right == 0:
        ##        textbox_left.text = f'{accept}'
        ##        textbox_right.text = f'{reject}'
        #        pos_k=[-0.2,-0.2]
        #if accept_reject[accept_reject_i] == 0: # reject
        #        pos_k=[1.5,0]
        #
        #
        #
        #accept_reject_i += 1
        textbox_left_2.reset()
        textbox_left_2.setText('')
        textbox_right_2.reset()
        textbox_right_2.setText('')
        # keep track of which components have finished
        observe_trial_averseComponents = [image2, textbox_left_2, textbox_right_2, polygon_2]
        for thisComponent in observe_trial_averseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "observe_trial_averse" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image2* updates
            
            # if image2 is starting this frame...
            if image2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image2.frameNStart = frameN  # exact frame index
                image2.tStart = t  # local t and not account for scr refresh
                image2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image2.started')
                # update status
                image2.status = STARTED
                image2.setAutoDraw(True)
            
            # if image2 is active this frame...
            if image2.status == STARTED:
                # update params
                image2.setImage(image_name, log=False)
            
            # if image2 is stopping this frame...
            if image2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image2.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    image2.tStop = t  # not accounting for scr refresh
                    image2.tStopRefresh = tThisFlipGlobal  # on global time
                    image2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image2.stopped')
                    # update status
                    image2.status = FINISHED
                    image2.setAutoDraw(False)
            # Run 'Each Frame' code from code_5
            if left_right == 1:
                textbox_left_2.text = f'{reject}'
                textbox_right_2.text = f'{accept}'
            elif left_right == 0:
                textbox_left_2.text = f'{accept}'
                textbox_right_2.text = f'{reject}'
            
            
            #
            ## Check if a key has been pressed
            #if key_resp.keys == 'left':
            #    pos_k=[-0.2,-0.2]
            #elif key_resp.keys == 'right':  # If any key other than 'right' is pressed
            #    pos_k=[0.2,-0.2]
            #else:  # If any key other than 'right' is pressed
            #    pos_k=[1.5,0]
            
            if accept_reject[accept_reject_i] == 1: # accept
                if left_right == 1:
            #        textbox_left.text = f'{reject}'
            #        textbox_right.text = f'{accept}'
                    pos_k=[0.2,-0.2]
                elif left_right == 0:
            #        textbox_left.text = f'{accept}'
            #        textbox_right.text = f'{reject}'
                    pos_k=[-0.2,-0.2]
            if accept_reject[accept_reject_i] == 0: # reject
                if left_right == 1:
            #        textbox_left.text = f'{reject}'
            #        textbox_right.text = f'{accept}'
                    pos_k=[-0.2,-0.2]
                elif left_right == 0:
            #        textbox_left.text = f'{accept}'
            #        textbox_right.text = f'{reject}'
                    pos_k=[0.2,-0.2]
            
            # *textbox_left_2* updates
            
            # if textbox_left_2 is starting this frame...
            if textbox_left_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_left_2.frameNStart = frameN  # exact frame index
                textbox_left_2.tStart = t  # local t and not account for scr refresh
                textbox_left_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_left_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_left_2.started')
                # update status
                textbox_left_2.status = STARTED
                textbox_left_2.setAutoDraw(True)
            
            # if textbox_left_2 is active this frame...
            if textbox_left_2.status == STARTED:
                # update params
                pass
            
            # if textbox_left_2 is stopping this frame...
            if textbox_left_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textbox_left_2.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    textbox_left_2.tStop = t  # not accounting for scr refresh
                    textbox_left_2.tStopRefresh = tThisFlipGlobal  # on global time
                    textbox_left_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox_left_2.stopped')
                    # update status
                    textbox_left_2.status = FINISHED
                    textbox_left_2.setAutoDraw(False)
            
            # *textbox_right_2* updates
            
            # if textbox_right_2 is starting this frame...
            if textbox_right_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_right_2.frameNStart = frameN  # exact frame index
                textbox_right_2.tStart = t  # local t and not account for scr refresh
                textbox_right_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_right_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_right_2.started')
                # update status
                textbox_right_2.status = STARTED
                textbox_right_2.setAutoDraw(True)
            
            # if textbox_right_2 is active this frame...
            if textbox_right_2.status == STARTED:
                # update params
                pass
            
            # if textbox_right_2 is stopping this frame...
            if textbox_right_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textbox_right_2.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    textbox_right_2.tStop = t  # not accounting for scr refresh
                    textbox_right_2.tStopRefresh = tThisFlipGlobal  # on global time
                    textbox_right_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox_right_2.stopped')
                    # update status
                    textbox_right_2.status = FINISHED
                    textbox_right_2.setAutoDraw(False)
            
            # *polygon_2* updates
            
            # if polygon_2 is starting this frame...
            if polygon_2.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                polygon_2.frameNStart = frameN  # exact frame index
                polygon_2.tStart = t  # local t and not account for scr refresh
                polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_2.started')
                # update status
                polygon_2.status = STARTED
                polygon_2.setAutoDraw(True)
            
            # if polygon_2 is active this frame...
            if polygon_2.status == STARTED:
                # update params
                polygon_2.setPos(pos_k, log=False)
            
            # if polygon_2 is stopping this frame...
            if polygon_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_2.tStop = t  # not accounting for scr refresh
                    polygon_2.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_2.stopped')
                    # update status
                    polygon_2.status = FINISHED
                    polygon_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in observe_trial_averseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "observe_trial_averse" ---
        for thisComponent in observe_trial_averseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('observe_trial_averse.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_4
        thisExp.addData('image_name_obs', image_name)
        # Run 'End Routine' code from code_5
        accept_reject_i += 1
        
        
        if left_right == 1:
            thisExp.addData('textbox_left_obs', 'Reject')
            thisExp.addData('textbox_right_obs', 'Accept')
        #    if key_resp.keys == 'left':
        #        thisExp.addData('selection', 'Reject')
        #    elif key_resp.keys == 'right':  # If any key other than 'right' is pressed
        #        thisExp.addData('selection', 'Accept')
        #    else:  # If any key other than 'right' is pressed
        #        thisExp.addData('selection', '')
            if accept_reject[accept_reject_i - 1] == 1:  # accept
                thisExp.addData('selection_obs', 'Reject')
            elif accept_reject[accept_reject_i - 1] == 0: # reject
                thisExp.addData('selection_obs', 'Accept')
        elif left_right == 0:
            thisExp.addData('textbox_left_obs', 'Accept')
            thisExp.addData('textbox_right_obs', 'Reject')
        #    if key_resp.keys == 'left':
        #        thisExp.addData('selection', 'Accept')
        #    elif key_resp.keys == 'right':  # If any key other than 'right' is pressed
        #        thisExp.addData('selection', 'Reject')
        #    else:  # If any key other than 'right' is pressed
        #        thisExp.addData('selection', '')
            if accept_reject[accept_reject_i - 1] == 1:  # accept
                thisExp.addData('selection_obs', 'Reject')
            elif accept_reject[accept_reject_i - 1] == 0: # reject
                thisExp.addData('selection_obs', 'Accept')
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        
        # --- Prepare to start Routine "third_click" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('third_click.started', globalClock.getTime(format='float'))
        text3_key_resp.keys = []
        text3_key_resp.rt = []
        _text3_key_resp_allKeys = []
        # keep track of which components have finished
        third_clickComponents = [text3, text3_key_resp]
        for thisComponent in third_clickComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "third_click" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text3* updates
            
            # if text3 is starting this frame...
            if text3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text3.frameNStart = frameN  # exact frame index
                text3.tStart = t  # local t and not account for scr refresh
                text3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text3.started')
                # update status
                text3.status = STARTED
                text3.setAutoDraw(True)
            
            # if text3 is active this frame...
            if text3.status == STARTED:
                # update params
                pass
            
            # *text3_key_resp* updates
            waitOnFlip = False
            
            # if text3_key_resp is starting this frame...
            if text3_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text3_key_resp.frameNStart = frameN  # exact frame index
                text3_key_resp.tStart = t  # local t and not account for scr refresh
                text3_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text3_key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text3_key_resp.started')
                # update status
                text3_key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(text3_key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(text3_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if text3_key_resp.status == STARTED and not waitOnFlip:
                theseKeys = text3_key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _text3_key_resp_allKeys.extend(theseKeys)
                if len(_text3_key_resp_allKeys):
                    text3_key_resp.keys = _text3_key_resp_allKeys[-1].name  # just the last key pressed
                    text3_key_resp.rt = _text3_key_resp_allKeys[-1].rt
                    text3_key_resp.duration = _text3_key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in third_clickComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "third_click" ---
        for thisComponent in third_clickComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('third_click.stopped', globalClock.getTime(format='float'))
        # check responses
        if text3_key_resp.keys in ['', [], None]:  # No response was made
            text3_key_resp.keys = None
        observe_trials_averse.addData('text3_key_resp.keys',text3_key_resp.keys)
        if text3_key_resp.keys != None:  # we had a response
            observe_trials_averse.addData('text3_key_resp.rt', text3_key_resp.rt)
            observe_trials_averse.addData('text3_key_resp.duration', text3_key_resp.duration)
        # the Routine "third_click" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'observe_trials_averse'
    
    
    # --- Prepare to start Routine "text_1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('text_1.started', globalClock.getTime(format='float'))
    text1_key_resp.keys = []
    text1_key_resp.rt = []
    _text1_key_resp_allKeys = []
    # keep track of which components have finished
    text_1Components = [text1, text1_key_resp]
    for thisComponent in text_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "text_1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text1* updates
        
        # if text1 is starting this frame...
        if text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text1.frameNStart = frameN  # exact frame index
            text1.tStart = t  # local t and not account for scr refresh
            text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text1.started')
            # update status
            text1.status = STARTED
            text1.setAutoDraw(True)
        
        # if text1 is active this frame...
        if text1.status == STARTED:
            # update params
            pass
        
        # *text1_key_resp* updates
        waitOnFlip = False
        
        # if text1_key_resp is starting this frame...
        if text1_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text1_key_resp.frameNStart = frameN  # exact frame index
            text1_key_resp.tStart = t  # local t and not account for scr refresh
            text1_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text1_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text1_key_resp.started')
            # update status
            text1_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(text1_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(text1_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if text1_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = text1_key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _text1_key_resp_allKeys.extend(theseKeys)
            if len(_text1_key_resp_allKeys):
                text1_key_resp.keys = _text1_key_resp_allKeys[-1].name  # just the last key pressed
                text1_key_resp.rt = _text1_key_resp_allKeys[-1].rt
                text1_key_resp.duration = _text1_key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in text_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "text_1" ---
    for thisComponent in text_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('text_1.stopped', globalClock.getTime(format='float'))
    # check responses
    if text1_key_resp.keys in ['', [], None]:  # No response was made
        text1_key_resp.keys = None
    thisExp.addData('text1_key_resp.keys',text1_key_resp.keys)
    if text1_key_resp.keys != None:  # we had a response
        thisExp.addData('text1_key_resp.rt', text1_key_resp.rt)
        thisExp.addData('text1_key_resp.duration', text1_key_resp.duration)
    thisExp.nextEntry()
    # the Routine "text_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    self_trials_2 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('award-probability.xlsx', selection='1:3'),
        seed=None, name='self_trials_2')
    thisExp.addLoop(self_trials_2)  # add the loop to the experiment
    thisSelf_trial_2 = self_trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSelf_trial_2.rgb)
    if thisSelf_trial_2 != None:
        for paramName in thisSelf_trial_2:
            globals()[paramName] = thisSelf_trial_2[paramName]
    
    for thisSelf_trial_2 in self_trials_2:
        currentLoop = self_trials_2
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisSelf_trial_2.rgb)
        if thisSelf_trial_2 != None:
            for paramName in thisSelf_trial_2:
                globals()[paramName] = thisSelf_trial_2[paramName]
        
        # --- Prepare to start Routine "intertrial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('intertrial.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code
        # Generate a uniform random number between 2 and 6
        inter_time = random.randint(2, 6)
        
        # keep track of which components have finished
        intertrialComponents = [fixation1]
        for thisComponent in intertrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "intertrial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation1* updates
            
            # if fixation1 is starting this frame...
            if fixation1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation1.frameNStart = frameN  # exact frame index
                fixation1.tStart = t  # local t and not account for scr refresh
                fixation1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation1.started')
                # update status
                fixation1.status = STARTED
                fixation1.setAutoDraw(True)
            
            # if fixation1 is active this frame...
            if fixation1.status == STARTED:
                # update params
                pass
            
            # if fixation1 is stopping this frame...
            if fixation1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation1.tStartRefresh + inter_time-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation1.tStop = t  # not accounting for scr refresh
                    fixation1.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation1.stopped')
                    # update status
                    fixation1.status = FINISHED
                    fixation1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in intertrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "intertrial" ---
        for thisComponent in intertrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('intertrial.stopped', globalClock.getTime(format='float'))
        # the Routine "intertrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "self_trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('self_trial.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_3
        left_right = random.randint(0, 1)
        
        
        textbox_left.reset()
        textbox_left.setText('')
        textbox_right.reset()
        textbox_right.setText('')
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        self_trialComponents = [image1, textbox_left, textbox_right, key_resp, polygon]
        for thisComponent in self_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "self_trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image1* updates
            
            # if image1 is starting this frame...
            if image1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image1.frameNStart = frameN  # exact frame index
                image1.tStart = t  # local t and not account for scr refresh
                image1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image1.started')
                # update status
                image1.status = STARTED
                image1.setAutoDraw(True)
            
            # if image1 is active this frame...
            if image1.status == STARTED:
                # update params
                image1.setImage(image_name, log=False)
            
            # if image1 is stopping this frame...
            if image1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image1.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    image1.tStop = t  # not accounting for scr refresh
                    image1.tStopRefresh = tThisFlipGlobal  # on global time
                    image1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image1.stopped')
                    # update status
                    image1.status = FINISHED
                    image1.setAutoDraw(False)
            # Run 'Each Frame' code from code_3
            if left_right == 1:
                textbox_left.text = f'{reject}'
                textbox_right.text = f'{accept}'
            elif left_right == 0:
                textbox_left.text = f'{accept}'
                textbox_right.text = f'{reject}'
            
            
            
            # Check if a key has been pressed
            if key_resp.keys == 'left':
                pos_k=[-0.2,-0.2]
            elif key_resp.keys == 'right':  # If any key other than 'right' is pressed
                pos_k=[0.2,-0.2]
            else:  # If any key other than 'right' is pressed
                pos_k=[1.5,0]
            
            
            
            # *textbox_left* updates
            
            # if textbox_left is starting this frame...
            if textbox_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_left.frameNStart = frameN  # exact frame index
                textbox_left.tStart = t  # local t and not account for scr refresh
                textbox_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_left, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_left.started')
                # update status
                textbox_left.status = STARTED
                textbox_left.setAutoDraw(True)
            
            # if textbox_left is active this frame...
            if textbox_left.status == STARTED:
                # update params
                pass
            
            # if textbox_left is stopping this frame...
            if textbox_left.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textbox_left.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    textbox_left.tStop = t  # not accounting for scr refresh
                    textbox_left.tStopRefresh = tThisFlipGlobal  # on global time
                    textbox_left.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox_left.stopped')
                    # update status
                    textbox_left.status = FINISHED
                    textbox_left.setAutoDraw(False)
            
            # *textbox_right* updates
            
            # if textbox_right is starting this frame...
            if textbox_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_right.frameNStart = frameN  # exact frame index
                textbox_right.tStart = t  # local t and not account for scr refresh
                textbox_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_right, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_right.started')
                # update status
                textbox_right.status = STARTED
                textbox_right.setAutoDraw(True)
            
            # if textbox_right is active this frame...
            if textbox_right.status == STARTED:
                # update params
                pass
            
            # if textbox_right is stopping this frame...
            if textbox_right.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textbox_right.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    textbox_right.tStop = t  # not accounting for scr refresh
                    textbox_right.tStopRefresh = tThisFlipGlobal  # on global time
                    textbox_right.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox_right.stopped')
                    # update status
                    textbox_right.status = FINISHED
                    textbox_right.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp is stopping this frame...
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.tStopRefresh = tThisFlipGlobal  # on global time
                    key_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp.stopped')
                    # update status
                    key_resp.status = FINISHED
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['right','left'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
            
            # *polygon* updates
            
            # if polygon is starting this frame...
            if polygon.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon.started')
                # update status
                polygon.status = STARTED
                polygon.setAutoDraw(True)
            
            # if polygon is active this frame...
            if polygon.status == STARTED:
                # update params
                polygon.setPos(pos_k, log=False)
            
            # if polygon is stopping this frame...
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.stopped')
                    # update status
                    polygon.status = FINISHED
                    polygon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in self_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "self_trial" ---
        for thisComponent in self_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('self_trial.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_2
        thisExp.addData('image_name', image_name)
        # Run 'End Routine' code from code_3
        if left_right == 1:
            thisExp.addData('textbox_left', 'Reject')
            thisExp.addData('textbox_right', 'Accept')
            if key_resp.keys == 'left':
                thisExp.addData('selection', 'Reject')
            elif key_resp.keys == 'right':  # If any key other than 'right' is pressed
                thisExp.addData('selection', 'Accept')
            else:  # If any key other than 'right' is pressed
                thisExp.addData('selection', '')
        elif left_right == 0:
            thisExp.addData('textbox_left', 'Accept')
            thisExp.addData('textbox_right', 'Reject')
            if key_resp.keys == 'left':
                thisExp.addData('selection', 'Accept')
            elif key_resp.keys == 'right':  # If any key other than 'right' is pressed
                thisExp.addData('selection', 'Reject')
            else:  # If any key other than 'right' is pressed
                thisExp.addData('selection', '')
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        self_trials_2.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            self_trials_2.addData('key_resp.rt', key_resp.rt)
            self_trials_2.addData('key_resp.duration', key_resp.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'self_trials_2'
    
    
    # --- Prepare to start Routine "text_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('text_3.started', globalClock.getTime(format='float'))
    text4_key_resp.keys = []
    text4_key_resp.rt = []
    _text4_key_resp_allKeys = []
    # keep track of which components have finished
    text_3Components = [text4, text4_key_resp]
    for thisComponent in text_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "text_3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text4* updates
        
        # if text4 is starting this frame...
        if text4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text4.frameNStart = frameN  # exact frame index
            text4.tStart = t  # local t and not account for scr refresh
            text4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text4.started')
            # update status
            text4.status = STARTED
            text4.setAutoDraw(True)
        
        # if text4 is active this frame...
        if text4.status == STARTED:
            # update params
            pass
        
        # *text4_key_resp* updates
        waitOnFlip = False
        
        # if text4_key_resp is starting this frame...
        if text4_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text4_key_resp.frameNStart = frameN  # exact frame index
            text4_key_resp.tStart = t  # local t and not account for scr refresh
            text4_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text4_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text4_key_resp.started')
            # update status
            text4_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(text4_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(text4_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if text4_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = text4_key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _text4_key_resp_allKeys.extend(theseKeys)
            if len(_text4_key_resp_allKeys):
                text4_key_resp.keys = _text4_key_resp_allKeys[-1].name  # just the last key pressed
                text4_key_resp.rt = _text4_key_resp_allKeys[-1].rt
                text4_key_resp.duration = _text4_key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in text_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "text_3" ---
    for thisComponent in text_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('text_3.stopped', globalClock.getTime(format='float'))
    # check responses
    if text4_key_resp.keys in ['', [], None]:  # No response was made
        text4_key_resp.keys = None
    thisExp.addData('text4_key_resp.keys',text4_key_resp.keys)
    if text4_key_resp.keys != None:  # we had a response
        thisExp.addData('text4_key_resp.rt', text4_key_resp.rt)
        thisExp.addData('text4_key_resp.duration', text4_key_resp.duration)
    thisExp.nextEntry()
    # the Routine "text_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    predict_trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('award-probability.xlsx', selection='1:3'),
        seed=None, name='predict_trials')
    thisExp.addLoop(predict_trials)  # add the loop to the experiment
    thisPredict_trial = predict_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPredict_trial.rgb)
    if thisPredict_trial != None:
        for paramName in thisPredict_trial:
            globals()[paramName] = thisPredict_trial[paramName]
    
    for thisPredict_trial in predict_trials:
        currentLoop = predict_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisPredict_trial.rgb)
        if thisPredict_trial != None:
            for paramName in thisPredict_trial:
                globals()[paramName] = thisPredict_trial[paramName]
        
        # --- Prepare to start Routine "intertrial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('intertrial.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code
        # Generate a uniform random number between 2 and 6
        inter_time = random.randint(2, 6)
        
        # keep track of which components have finished
        intertrialComponents = [fixation1]
        for thisComponent in intertrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "intertrial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation1* updates
            
            # if fixation1 is starting this frame...
            if fixation1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation1.frameNStart = frameN  # exact frame index
                fixation1.tStart = t  # local t and not account for scr refresh
                fixation1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation1.started')
                # update status
                fixation1.status = STARTED
                fixation1.setAutoDraw(True)
            
            # if fixation1 is active this frame...
            if fixation1.status == STARTED:
                # update params
                pass
            
            # if fixation1 is stopping this frame...
            if fixation1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation1.tStartRefresh + inter_time-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation1.tStop = t  # not accounting for scr refresh
                    fixation1.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation1.stopped')
                    # update status
                    fixation1.status = FINISHED
                    fixation1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in intertrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "intertrial" ---
        for thisComponent in intertrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('intertrial.stopped', globalClock.getTime(format='float'))
        # the Routine "intertrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "predict_trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('predict_trial.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_7
        left_right = random.randint(0, 1)
        
        
        textbox_left_3.reset()
        textbox_left_3.setText('')
        textbox_right_3.reset()
        textbox_right_3.setText('')
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        predict_trialComponents = [image3, textbox_left_3, textbox_right_3, key_resp_2, polygon_3]
        for thisComponent in predict_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "predict_trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image3* updates
            
            # if image3 is starting this frame...
            if image3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image3.frameNStart = frameN  # exact frame index
                image3.tStart = t  # local t and not account for scr refresh
                image3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image3.started')
                # update status
                image3.status = STARTED
                image3.setAutoDraw(True)
            
            # if image3 is active this frame...
            if image3.status == STARTED:
                # update params
                image3.setImage(image_name, log=False)
            
            # if image3 is stopping this frame...
            if image3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image3.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    image3.tStop = t  # not accounting for scr refresh
                    image3.tStopRefresh = tThisFlipGlobal  # on global time
                    image3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image3.stopped')
                    # update status
                    image3.status = FINISHED
                    image3.setAutoDraw(False)
            # Run 'Each Frame' code from code_7
            if left_right == 1:
                textbox_left_3.text = f'{reject}'
                textbox_right_3.text = f'{accept}'
            elif left_right == 0:
                textbox_left_3.text = f'{accept}'
                textbox_right_3.text = f'{reject}'
            
            
            
            # Check if a key has been pressed
            if key_resp_2.keys == 'left':
                pos_k=[-0.2,-0.2]
            elif key_resp_2.keys == 'right':  # If any key other than 'right' is pressed
                pos_k=[0.2,-0.2]
            else:  # If any key other than 'right' is pressed
                pos_k=[1.5,0]
            
            
            
            # *textbox_left_3* updates
            
            # if textbox_left_3 is starting this frame...
            if textbox_left_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_left_3.frameNStart = frameN  # exact frame index
                textbox_left_3.tStart = t  # local t and not account for scr refresh
                textbox_left_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_left_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_left_3.started')
                # update status
                textbox_left_3.status = STARTED
                textbox_left_3.setAutoDraw(True)
            
            # if textbox_left_3 is active this frame...
            if textbox_left_3.status == STARTED:
                # update params
                pass
            
            # if textbox_left_3 is stopping this frame...
            if textbox_left_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textbox_left_3.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    textbox_left_3.tStop = t  # not accounting for scr refresh
                    textbox_left_3.tStopRefresh = tThisFlipGlobal  # on global time
                    textbox_left_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox_left_3.stopped')
                    # update status
                    textbox_left_3.status = FINISHED
                    textbox_left_3.setAutoDraw(False)
            
            # *textbox_right_3* updates
            
            # if textbox_right_3 is starting this frame...
            if textbox_right_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_right_3.frameNStart = frameN  # exact frame index
                textbox_right_3.tStart = t  # local t and not account for scr refresh
                textbox_right_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_right_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_right_3.started')
                # update status
                textbox_right_3.status = STARTED
                textbox_right_3.setAutoDraw(True)
            
            # if textbox_right_3 is active this frame...
            if textbox_right_3.status == STARTED:
                # update params
                pass
            
            # if textbox_right_3 is stopping this frame...
            if textbox_right_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textbox_right_3.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    textbox_right_3.tStop = t  # not accounting for scr refresh
                    textbox_right_3.tStopRefresh = tThisFlipGlobal  # on global time
                    textbox_right_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox_right_3.stopped')
                    # update status
                    textbox_right_3.status = FINISHED
                    textbox_right_3.setAutoDraw(False)
            
            # *key_resp_2* updates
            waitOnFlip = False
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2.started')
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_2 is stopping this frame...
            if key_resp_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_2.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_2.tStop = t  # not accounting for scr refresh
                    key_resp_2.tStopRefresh = tThisFlipGlobal  # on global time
                    key_resp_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_2.stopped')
                    # update status
                    key_resp_2.status = FINISHED
                    key_resp_2.status = FINISHED
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['right','left'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    key_resp_2.duration = _key_resp_2_allKeys[-1].duration
            
            # *polygon_3* updates
            
            # if polygon_3 is starting this frame...
            if polygon_3.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                polygon_3.frameNStart = frameN  # exact frame index
                polygon_3.tStart = t  # local t and not account for scr refresh
                polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_3.started')
                # update status
                polygon_3.status = STARTED
                polygon_3.setAutoDraw(True)
            
            # if polygon_3 is active this frame...
            if polygon_3.status == STARTED:
                # update params
                polygon_3.setPos(pos_k, log=False)
            
            # if polygon_3 is stopping this frame...
            if polygon_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_3.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_3.tStop = t  # not accounting for scr refresh
                    polygon_3.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_3.stopped')
                    # update status
                    polygon_3.status = FINISHED
                    polygon_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in predict_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "predict_trial" ---
        for thisComponent in predict_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('predict_trial.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_6
        thisExp.addData('image_name_pred', image_name)
        # Run 'End Routine' code from code_7
        if left_right == 1:
            thisExp.addData('textbox_left_pred', 'Reject')
            thisExp.addData('textbox_right_pred', 'Accept')
            if key_resp_2.keys == 'left':
                thisExp.addData('selection_pred', 'Reject')
            elif key_resp_2.keys == 'right':  # If any key other than 'right' is pressed
                thisExp.addData('selection_pred', 'Accept')
            else:  # If any key other than 'right' is pressed
                thisExp.addData('selection', '')
        elif left_right == 0:
            thisExp.addData('textbox_left_pred', 'Accept')
            thisExp.addData('textbox_right_pred', 'Reject')
            if key_resp_2.keys == 'left':
                thisExp.addData('selection_pred', 'Accept')
            elif key_resp_2.keys == 'right':  # If any key other than 'right' is pressed
                thisExp.addData('selection_pred', 'Reject')
            else:  # If any key other than 'right' is pressed
                thisExp.addData('selection_pred', '')
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        predict_trials.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            predict_trials.addData('key_resp_2.rt', key_resp_2.rt)
            predict_trials.addData('key_resp_2.duration', key_resp_2.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'predict_trials'
    
    
    # --- Prepare to start Routine "text_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('text_2.started', globalClock.getTime(format='float'))
    text2_key_resp.keys = []
    text2_key_resp.rt = []
    _text2_key_resp_allKeys = []
    # keep track of which components have finished
    text_2Components = [text2, text2_key_resp]
    for thisComponent in text_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "text_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text2* updates
        
        # if text2 is starting this frame...
        if text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text2.frameNStart = frameN  # exact frame index
            text2.tStart = t  # local t and not account for scr refresh
            text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text2.started')
            # update status
            text2.status = STARTED
            text2.setAutoDraw(True)
        
        # if text2 is active this frame...
        if text2.status == STARTED:
            # update params
            pass
        
        # *text2_key_resp* updates
        waitOnFlip = False
        
        # if text2_key_resp is starting this frame...
        if text2_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text2_key_resp.frameNStart = frameN  # exact frame index
            text2_key_resp.tStart = t  # local t and not account for scr refresh
            text2_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text2_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text2_key_resp.started')
            # update status
            text2_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(text2_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(text2_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if text2_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = text2_key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _text2_key_resp_allKeys.extend(theseKeys)
            if len(_text2_key_resp_allKeys):
                text2_key_resp.keys = _text2_key_resp_allKeys[-1].name  # just the last key pressed
                text2_key_resp.rt = _text2_key_resp_allKeys[-1].rt
                text2_key_resp.duration = _text2_key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in text_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "text_2" ---
    for thisComponent in text_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('text_2.stopped', globalClock.getTime(format='float'))
    # check responses
    if text2_key_resp.keys in ['', [], None]:  # No response was made
        text2_key_resp.keys = None
    thisExp.addData('text2_key_resp.keys',text2_key_resp.keys)
    if text2_key_resp.keys != None:  # we had a response
        thisExp.addData('text2_key_resp.rt', text2_key_resp.rt)
        thisExp.addData('text2_key_resp.duration', text2_key_resp.duration)
    thisExp.nextEntry()
    # the Routine "text_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    observe_trials_seek = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('award-probability.xlsx', selection='1:3'),
        seed=None, name='observe_trials_seek')
    thisExp.addLoop(observe_trials_seek)  # add the loop to the experiment
    thisObserve_trials_seek = observe_trials_seek.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisObserve_trials_seek.rgb)
    if thisObserve_trials_seek != None:
        for paramName in thisObserve_trials_seek:
            globals()[paramName] = thisObserve_trials_seek[paramName]
    
    for thisObserve_trials_seek in observe_trials_seek:
        currentLoop = observe_trials_seek
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisObserve_trials_seek.rgb)
        if thisObserve_trials_seek != None:
            for paramName in thisObserve_trials_seek:
                globals()[paramName] = thisObserve_trials_seek[paramName]
        
        # --- Prepare to start Routine "intertrial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('intertrial.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code
        # Generate a uniform random number between 2 and 6
        inter_time = random.randint(2, 6)
        
        # keep track of which components have finished
        intertrialComponents = [fixation1]
        for thisComponent in intertrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "intertrial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation1* updates
            
            # if fixation1 is starting this frame...
            if fixation1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation1.frameNStart = frameN  # exact frame index
                fixation1.tStart = t  # local t and not account for scr refresh
                fixation1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation1.started')
                # update status
                fixation1.status = STARTED
                fixation1.setAutoDraw(True)
            
            # if fixation1 is active this frame...
            if fixation1.status == STARTED:
                # update params
                pass
            
            # if fixation1 is stopping this frame...
            if fixation1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation1.tStartRefresh + inter_time-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation1.tStop = t  # not accounting for scr refresh
                    fixation1.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation1.stopped')
                    # update status
                    fixation1.status = FINISHED
                    fixation1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in intertrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "intertrial" ---
        for thisComponent in intertrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('intertrial.stopped', globalClock.getTime(format='float'))
        # the Routine "intertrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "observe_trial_seek" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('observe_trial_seek.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_9
        left_right = random.randint(0, 1)
        
        
        #
        #if accept_reject[accept_reject_i] == 1: # accept
        #    if left_right == 1:
        ##        textbox_left.text = f'{reject}'
        ##        textbox_right.text = f'{accept}'
        #        pos_k=[0.2,-0.2]
        #    elif left_right == 0:
        ##        textbox_left.text = f'{accept}'
        ##        textbox_right.text = f'{reject}'
        #        pos_k=[-0.2,-0.2]
        #if accept_reject[accept_reject_i] == 0: # reject
        #        pos_k=[1.5,0]
        #
        #
        #
        #accept_reject_i += 1
        textbox_left_4.reset()
        textbox_left_4.setText('')
        textbox_right_4.reset()
        textbox_right_4.setText('')
        # keep track of which components have finished
        observe_trial_seekComponents = [image4, textbox_left_4, textbox_right_4, polygon_4]
        for thisComponent in observe_trial_seekComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "observe_trial_seek" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image4* updates
            
            # if image4 is starting this frame...
            if image4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image4.frameNStart = frameN  # exact frame index
                image4.tStart = t  # local t and not account for scr refresh
                image4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image4.started')
                # update status
                image4.status = STARTED
                image4.setAutoDraw(True)
            
            # if image4 is active this frame...
            if image4.status == STARTED:
                # update params
                image4.setImage(image_name, log=False)
            
            # if image4 is stopping this frame...
            if image4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image4.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    image4.tStop = t  # not accounting for scr refresh
                    image4.tStopRefresh = tThisFlipGlobal  # on global time
                    image4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image4.stopped')
                    # update status
                    image4.status = FINISHED
                    image4.setAutoDraw(False)
            # Run 'Each Frame' code from code_9
            if left_right == 1:
                textbox_left_4.text = f'{reject}'
                textbox_right_4.text = f'{accept}'
            elif left_right == 0:
                textbox_left_4.text = f'{accept}'
                textbox_right_4.text = f'{reject}'
            
            
            #
            ## Check if a key has been pressed
            #if key_resp.keys == 'left':
            #    pos_k=[-0.2,-0.2]
            #elif key_resp.keys == 'right':  # If any key other than 'right' is pressed
            #    pos_k=[0.2,-0.2]
            #else:  # If any key other than 'right' is pressed
            #    pos_k=[1.5,0]
            
            if accept_reject_2[accept_reject_i_2] == 1: # accept
                if left_right == 1:
            #        textbox_left.text = f'{reject}'
            #        textbox_right.text = f'{accept}'
                    pos_k=[0.2,-0.2]
                elif left_right == 0:
            #        textbox_left.text = f'{accept}'
            #        textbox_right.text = f'{reject}'
                    pos_k=[-0.2,-0.2]
            if accept_reject_2[accept_reject_i_2] == 0: # reject
                if left_right == 1:
            #        textbox_left.text = f'{reject}'
            #        textbox_right.text = f'{accept}'
                    pos_k=[-0.2,-0.2]
                elif left_right == 0:
            #        textbox_left.text = f'{accept}'
            #        textbox_right.text = f'{reject}'
                    pos_k=[0.2,-0.2]
            
            # *textbox_left_4* updates
            
            # if textbox_left_4 is starting this frame...
            if textbox_left_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_left_4.frameNStart = frameN  # exact frame index
                textbox_left_4.tStart = t  # local t and not account for scr refresh
                textbox_left_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_left_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_left_4.started')
                # update status
                textbox_left_4.status = STARTED
                textbox_left_4.setAutoDraw(True)
            
            # if textbox_left_4 is active this frame...
            if textbox_left_4.status == STARTED:
                # update params
                pass
            
            # if textbox_left_4 is stopping this frame...
            if textbox_left_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textbox_left_4.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    textbox_left_4.tStop = t  # not accounting for scr refresh
                    textbox_left_4.tStopRefresh = tThisFlipGlobal  # on global time
                    textbox_left_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox_left_4.stopped')
                    # update status
                    textbox_left_4.status = FINISHED
                    textbox_left_4.setAutoDraw(False)
            
            # *textbox_right_4* updates
            
            # if textbox_right_4 is starting this frame...
            if textbox_right_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_right_4.frameNStart = frameN  # exact frame index
                textbox_right_4.tStart = t  # local t and not account for scr refresh
                textbox_right_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_right_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_right_4.started')
                # update status
                textbox_right_4.status = STARTED
                textbox_right_4.setAutoDraw(True)
            
            # if textbox_right_4 is active this frame...
            if textbox_right_4.status == STARTED:
                # update params
                pass
            
            # if textbox_right_4 is stopping this frame...
            if textbox_right_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textbox_right_4.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    textbox_right_4.tStop = t  # not accounting for scr refresh
                    textbox_right_4.tStopRefresh = tThisFlipGlobal  # on global time
                    textbox_right_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox_right_4.stopped')
                    # update status
                    textbox_right_4.status = FINISHED
                    textbox_right_4.setAutoDraw(False)
            
            # *polygon_4* updates
            
            # if polygon_4 is starting this frame...
            if polygon_4.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                polygon_4.frameNStart = frameN  # exact frame index
                polygon_4.tStart = t  # local t and not account for scr refresh
                polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_4.started')
                # update status
                polygon_4.status = STARTED
                polygon_4.setAutoDraw(True)
            
            # if polygon_4 is active this frame...
            if polygon_4.status == STARTED:
                # update params
                polygon_4.setPos(pos_k, log=False)
            
            # if polygon_4 is stopping this frame...
            if polygon_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_4.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_4.tStop = t  # not accounting for scr refresh
                    polygon_4.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_4.stopped')
                    # update status
                    polygon_4.status = FINISHED
                    polygon_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in observe_trial_seekComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "observe_trial_seek" ---
        for thisComponent in observe_trial_seekComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('observe_trial_seek.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_8
        thisExp.addData('image_name_obs_2', image_name)
        # Run 'End Routine' code from code_9
        accept_reject_i_2 += 1
        
        
        if left_right == 1:
            thisExp.addData('textbox_left_obs_2', 'Reject')
            thisExp.addData('textbox_right_obs_2', 'Accept')
        #    if key_resp.keys == 'left':
        #        thisExp.addData('selection', 'Reject')
        #    elif key_resp.keys == 'right':  # If any key other than 'right' is pressed
        #        thisExp.addData('selection', 'Accept')
        #    else:  # If any key other than 'right' is pressed
        #        thisExp.addData('selection', '')
            if accept_reject_2[accept_reject_i_2 - 1] == 1:  # accept
                thisExp.addData('selection_obs_2', 'Reject')
            elif accept_reject_2[accept_reject_i_2 - 1] == 0: # reject
                thisExp.addData('selection_obs_2', 'Accept')
        elif left_right == 0:
            thisExp.addData('textbox_left_obs_2', 'Accept')
            thisExp.addData('textbox_right_obs_2', 'Reject')
        #    if key_resp.keys == 'left':
        #        thisExp.addData('selection', 'Accept')
        #    elif key_resp.keys == 'right':  # If any key other than 'right' is pressed
        #        thisExp.addData('selection', 'Reject')
        #    else:  # If any key other than 'right' is pressed
        #        thisExp.addData('selection', '')
            if accept_reject_2[accept_reject_i_2 - 1] == 1:  # accept
                thisExp.addData('selection_obs_2', 'Reject')
            elif accept_reject_2[accept_reject_i_2 - 1] == 0: # reject
                thisExp.addData('selection_obs_2', 'Accept')
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        
        # --- Prepare to start Routine "third_click" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('third_click.started', globalClock.getTime(format='float'))
        text3_key_resp.keys = []
        text3_key_resp.rt = []
        _text3_key_resp_allKeys = []
        # keep track of which components have finished
        third_clickComponents = [text3, text3_key_resp]
        for thisComponent in third_clickComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "third_click" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text3* updates
            
            # if text3 is starting this frame...
            if text3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text3.frameNStart = frameN  # exact frame index
                text3.tStart = t  # local t and not account for scr refresh
                text3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text3.started')
                # update status
                text3.status = STARTED
                text3.setAutoDraw(True)
            
            # if text3 is active this frame...
            if text3.status == STARTED:
                # update params
                pass
            
            # *text3_key_resp* updates
            waitOnFlip = False
            
            # if text3_key_resp is starting this frame...
            if text3_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text3_key_resp.frameNStart = frameN  # exact frame index
                text3_key_resp.tStart = t  # local t and not account for scr refresh
                text3_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text3_key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text3_key_resp.started')
                # update status
                text3_key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(text3_key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(text3_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if text3_key_resp.status == STARTED and not waitOnFlip:
                theseKeys = text3_key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _text3_key_resp_allKeys.extend(theseKeys)
                if len(_text3_key_resp_allKeys):
                    text3_key_resp.keys = _text3_key_resp_allKeys[-1].name  # just the last key pressed
                    text3_key_resp.rt = _text3_key_resp_allKeys[-1].rt
                    text3_key_resp.duration = _text3_key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in third_clickComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "third_click" ---
        for thisComponent in third_clickComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('third_click.stopped', globalClock.getTime(format='float'))
        # check responses
        if text3_key_resp.keys in ['', [], None]:  # No response was made
            text3_key_resp.keys = None
        observe_trials_seek.addData('text3_key_resp.keys',text3_key_resp.keys)
        if text3_key_resp.keys != None:  # we had a response
            observe_trials_seek.addData('text3_key_resp.rt', text3_key_resp.rt)
            observe_trials_seek.addData('text3_key_resp.duration', text3_key_resp.duration)
        # the Routine "third_click" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'observe_trials_seek'
    
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
