#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.4),
    on May 28, 2024, at 14:11
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
expName = 'article1'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'learning type': '1',
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
        originPath='D:\\UT\\semester 4 - courses\\Cognitive science\\HWs\\HW1\\answer\\article1\\article1.py',
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
            monitor='testMonitor', color='white', colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = 'white'
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
    if deviceManager.getDevice('text0_key_resp') is None:
        # initialise text0_key_resp
        text0_key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='text0_key_resp',
        )
    if deviceManager.getDevice('key_resp_0') is None:
        # initialise key_resp_0
        key_resp_0 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_0',
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
    if deviceManager.getDevice('text2_key_resp') is None:
        # initialise text2_key_resp
        text2_key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='text2_key_resp',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
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
    
    # --- Initialize components for Routine "text_0" ---
    text0 = visual.TextStim(win=win, name='text0',
        text='هر بار از میان دو گزینه\u200cی نمایش داده شده،\nبا فشردن یکی از کلیدهای راست و چپ روی کیبورد،\n گزینه\u200cی با بیشترین پاداش را انتخاب کنید.\n\n(هرگاه آماده بودید، کلید space را فشار دهید.)',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    text0_key_resp = keyboard.Keyboard(deviceName='text0_key_resp')
    
    # --- Initialize components for Routine "fixation_training" ---
    fixation0 = visual.ShapeStim(
        win=win, name='fixation0', vertices='cross',units='norm', 
        size=(0.03, 0.06),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=0.08,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor='black',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "main_training" ---
    # Run 'Begin Experiment' code from training_code
    # Begin Experiment
    
    import random
    
    # Create a list of image pairs
    image_pairs0 = [
        ("1-1.jpg", "1-2.jpg"),
        ("1-3.jpg", "1-4.jpg"),
        ("1-2.jpg", "1-1.jpg"),
        ("1-4.jpg", "1-3.jpg")
    ]
    
    # Create a list of trials with each pair in both possible positions
    trials0 = []
    for pair in image_pairs0:
        trials0.append(pair)        # Original order
        #trials.append(pair[::-1])  # Reversed order
    
    # Multiply trials to ensure enough repetitions and shuffle
    trials0 *= 5  # Adjust the number of repetitions as needed
    random.shuffle(trials0)
    #
    ### Initialize PsychoPy window
    ##win = visual.Window(size=(800, 600), units='pix', fullscr=False)
    #win = visual.Window(size=(800, 600), monitor="testMonitor")
    
    # Initialize current_trial
    current_trial0 = 0
    
    #
    #image_filenames = ["1.jpg", "2.jpg", "3.jpg", "4.jpg"]  # Add all your filenames here
    #
    ## Create an empty list to store ImageStim objects
    #image_stims = []
    #
    ## Create ImageStim objects for each filename
    #for filename in image_filenames:
    #    image_stim = visual.ImageStim(win, image=filename, pos=(0, 0))  # Adjust position if needed
    #    image_stims.append(image_stim)
    #
    #
    left_image_0 = visual.ImageStim(
        win=win,
        name='left_image_0', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.5, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    right_image_0 = visual.ImageStim(
        win=win,
        name='right_image_0', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.5, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    key_resp_0 = keyboard.Keyboard(deviceName='key_resp_0')
    # Run 'Begin Experiment' code from code_0
    import numpy as np
    
    
    pos_k0 =(0,0)
    
    l_type = expInfo['learning type']
    
    #no_response = False
    polygon_0 = visual.Rect(
        win=win, name='polygon_0',
        width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=20.0,     colorSpace='rgb',  lineColor=[-0.5765, 0.0039, 1.0000], fillColor=[0.0000, 0.0000, 0.0000],
        opacity=0.3, depth=-5.0, interpolate=True)
    left_learning_reward_0 = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         pos=(-0.5, -0.3),     letterHeight=0.05,
         size=(0.6, 0.6), borderWidth=2.0,
         color=[-0.5765, 0.0039, 1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='left_learning_reward_0',
         depth=-6, autoLog=True,
    )
    right_learning_reward_0 = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         pos=(0.5, -0.3),     letterHeight=0.05,
         size=(0.6, 0.6), borderWidth=2.0,
         color=[-0.5765, 0.0039, 1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='right_learning_reward_0',
         depth=-7, autoLog=True,
    )
    text_no_resp_0 = visual.TextStim(win=win, name='text_no_resp_0',
        text='',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-8.0);
    
    # --- Initialize components for Routine "text_1" ---
    text1 = visual.TextStim(win=win, name='text1',
        text='هر بار از میان دو گزینه\u200cی نمایش داده شده،\nبا فشردن یکی از کلیدهای راست و چپ روی کیبورد،\n گزینه\u200cی با بیشترین پاداش را انتخاب کنید.\n\n(مجموع پاداش\u200cهای شما در این بخش،\nپاداش نهایی شما را تعیین خواهد کرد.)\n\n(هرگاه آماده بودید، کلید space را فشار دهید.)',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    text1_key_resp = keyboard.Keyboard(deviceName='text1_key_resp')
    
    # --- Initialize components for Routine "fixation_learning" ---
    fixation1 = visual.ShapeStim(
        win=win, name='fixation1', vertices='cross',units='norm', 
        size=(0.03, 0.06),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=0.08,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor='black',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "main_learning" ---
    # Run 'Begin Experiment' code from learning_code
    # Begin Experiment
    
    import random
    
    # Create a list of image pairs
    image_pairs = [
        ("1.jpg", "2.jpg"),
        ("3.jpg", "4.jpg"),
        ("2.jpg", "1.jpg"),
        ("4.jpg", "3.jpg")
    ]
    
    # Create a list of trials with each pair in both possible positions
    trials = []
    for pair in image_pairs:
        trials.append(pair)        # Original order
        #trials.append(pair[::-1])  # Reversed order
    
    # Multiply trials to ensure enough repetitions and shuffle
    trials *= 25  # Adjust the number of repetitions as needed
    random.shuffle(trials)
    #
    ### Initialize PsychoPy window
    ##win = visual.Window(size=(800, 600), units='pix', fullscr=False)
    #win = visual.Window(size=(800, 600), monitor="testMonitor")
    
    # Initialize current_trial
    current_trial = 0
    
    #
    #image_filenames = ["1.jpg", "2.jpg", "3.jpg", "4.jpg"]  # Add all your filenames here
    #
    ## Create an empty list to store ImageStim objects
    #image_stims = []
    #
    ## Create ImageStim objects for each filename
    #for filename in image_filenames:
    #    image_stim = visual.ImageStim(win, image=filename, pos=(0, 0))  # Adjust position if needed
    #    image_stims.append(image_stim)
    #
    #
    left_image = visual.ImageStim(
        win=win,
        name='left_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.5, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    right_image = visual.ImageStim(
        win=win,
        name='right_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.5, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    # Run 'Begin Experiment' code from code
    import numpy as np
    
    
    pos_k =(0,0)
    
    l_type = expInfo['learning type']
    
    #no_response = False
    
    # Initialize an empty array (list)
    rewards_array = []
    
    polygon = visual.Rect(
        win=win, name='polygon',
        width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=20.0,     colorSpace='rgb',  lineColor=[-0.5765, 0.0039, 1.0000], fillColor=[0.0000, 0.0000, 0.0000],
        opacity=0.3, depth=-5.0, interpolate=True)
    left_learning_reward = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         pos=(-0.5, -0.3),     letterHeight=0.05,
         size=(0.6, 0.6), borderWidth=2.0,
         color=[-0.5765, 0.0039, 1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='left_learning_reward',
         depth=-6, autoLog=True,
    )
    right_learning_reward = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         pos=(0.5, -0.3),     letterHeight=0.05,
         size=(0.6, 0.6), borderWidth=2.0,
         color=[-0.5765, 0.0039, 1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='right_learning_reward',
         depth=-7, autoLog=True,
    )
    text_no_resp = visual.TextStim(win=win, name='text_no_resp',
        text='',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-8.0);
    
    # --- Initialize components for Routine "text_2" ---
    text2 = visual.TextStim(win=win, name='text2',
        text='هر بار از میان دو گزینه\u200cی نمایش داده شده،\nبا فشردن یکی از کلیدهای راست و چپ روی کیبورد،\n گزینه\u200cی با بیشترین پاداش را انتخاب کنید.\n\nتوجه:\nدر این بخش ممکن است جفت عددهایی را مقایسه کنید \nکه در بخش قبل مقایسه نکرده بودید.\n\nپس از انتخاب یکی از دو گزینه\u200cی نمایش داده شده\nباید میزان اطمینان خود از انتخابتان را با استفاده از موس\nمشخص کنید.\n\n(هرگاه آماده بودید، کلید space را فشار دهید.)',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    text2_key_resp = keyboard.Keyboard(deviceName='text2_key_resp')
    
    # --- Initialize components for Routine "fixation_transfer" ---
    fixation2 = visual.ShapeStim(
        win=win, name='fixation2', vertices='cross',units='norm', 
        size=(0.03, 0.06),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=0.08,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor='black',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "main_transfer" ---
    # Run 'Begin Experiment' code from transfer_code
    # Begin Experiment
    
    import random
    
    # Create a list of image pairs
    image_pairs_2 = [
        ("1.jpg", "2.jpg"),
        ("1.jpg", "3.jpg"),
        ("1.jpg", "4.jpg"),
        ("2.jpg", "3.jpg"),
        ("2.jpg", "4.jpg"),
        ("3.jpg", "4.jpg")
    ]
    
    # Create a list of trials with each pair in both possible positions
    trials_2 = []
    for pair in image_pairs_2:
        trials_2.append(pair)        # Original order
        #trials.append(pair[::-1])  # Reversed order
    
    # Multiply trials to ensure enough repetitions and shuffle
    trials_2 *= 4  # Adjust the number of repetitions as needed
    random.shuffle(trials_2)
    #
    ### Initialize PsychoPy window
    ##win = visual.Window(size=(800, 600), units='pix', fullscr=False)
    #win = visual.Window(size=(800, 600), monitor="testMonitor")
    
    # Initialize current_trial
    current_trial_2 = 0
    
    #
    #image_filenames = ["1.jpg", "2.jpg", "3.jpg", "4.jpg"]  # Add all your filenames here
    #
    ## Create an empty list to store ImageStim objects
    #image_stims = []
    #
    ## Create ImageStim objects for each filename
    #for filename in image_filenames:
    #    image_stim = visual.ImageStim(win, image=filename, pos=(0, 0))  # Adjust position if needed
    #    image_stims.append(image_stim)
    #
    #
    left_image_2 = visual.ImageStim(
        win=win,
        name='left_image_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.5, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    right_image_2 = visual.ImageStim(
        win=win,
        name='right_image_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.5, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    # Run 'Begin Experiment' code from code_2
    import numpy as np
    
    
    pos_k_2 =(0,0)
    
    
    polygon_2 = visual.Rect(
        win=win, name='polygon_2',
        width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=20.0,     colorSpace='rgb',  lineColor=[-0.5765, 0.0039, 1.0000], fillColor=[0.0000, 0.0000, 0.0000],
        opacity=0.3, depth=-5.0, interpolate=True)
    
    # --- Initialize components for Routine "slider_transfer" ---
    slider_trns = visual.Slider(win=win, name='slider_trns',
        startValue=50, size=(1.0, 0.1), pos=(0, 0), units=win.units,
        labels=(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100), ticks=(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100), granularity=5.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='Black', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=0, readOnly=False)
    mouse_trns = event.Mouse(win=win)
    x, y = [None, None]
    mouse_trns.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "text_3" ---
    text3 = visual.TextStim(win=win, name='text3',
        text='برای هر تصویر نمایش داده شده\nمیزان برآورد خود از پاداش مربوط به آن را \nبا استفاده از موس مشخص کنید.\n\n(هرگاه آماده بودید، کلید space را فشار دهید.)',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    text3_key_resp = keyboard.Keyboard(deviceName='text3_key_resp')
    
    # --- Initialize components for Routine "fixation_estimation" ---
    fixation3 = visual.ShapeStim(
        win=win, name='fixation3', vertices='cross',units='norm', 
        size=(0.03, 0.06),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=0.08,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor='black',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "main_estimation" ---
    # Run 'Begin Experiment' code from estimation_code
    # Begin Experiment
    
    import random
    
    # Create a list of image pairs
    images3 = [
        "1.jpg",
        "2.jpg",
        "3.jpg",
        "4.jpg"
    ]
    
    # Create a list of trials with each pair in both possible positions
    trials_3 = []
    for image in images3:
        trials_3.append(image)        # Original order
        #trials.append(pair[::-1])  # Reversed order
    
    # Multiply trials to ensure enough repetitions and shuffle
    trials_3 *= 4  # Adjust the number of repetitions as needed
    random.shuffle(trials_3)
    #
    ### Initialize PsychoPy window
    ##win = visual.Window(size=(800, 600), units='pix', fullscr=False)
    #win = visual.Window(size=(800, 600), monitor="testMonitor")
    
    # Initialize current_trial
    current_trial_3 = 0
    
    #
    #image_filenames = ["1.jpg", "2.jpg", "3.jpg", "4.jpg"]  # Add all your filenames here
    #
    ## Create an empty list to store ImageStim objects
    #image_stims = []
    #
    ## Create ImageStim objects for each filename
    #for filename in image_filenames:
    #    image_stim = visual.ImageStim(win, image=filename, pos=(0, 0))  # Adjust position if needed
    #    image_stims.append(image_stim)
    #
    #
    image_3 = visual.ImageStim(
        win=win,
        name='image_3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.2), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    slider_estm = visual.Slider(win=win, name='slider_estm',
        startValue=50, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
        labels=(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100), ticks=(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100), granularity=5.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='Black', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-2, readOnly=False)
    mouse_estm = event.Mouse(win=win)
    x, y = [None, None]
    mouse_estm.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "show_reward" ---
    text4 = visual.TextStim(win=win, name='text4',
        text='مجموع پاداش\u200c (با توجه به گزینه\u200cهای فاز یادگیری):\n',
        font='Arial',
        pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    totalRewardText = visual.TextStim(win=win, name='totalRewardText',
        text=None,
        font='Arial',
        pos=(0, -0.1), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-1.0);
    # Run 'Begin Experiment' code from code_5
    # Initialize the total reward
    total_reward = 0
    
    
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
    
    # --- Prepare to start Routine "text_0" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('text_0.started', globalClock.getTime(format='float'))
    text0_key_resp.keys = []
    text0_key_resp.rt = []
    _text0_key_resp_allKeys = []
    # keep track of which components have finished
    text_0Components = [text0, text0_key_resp]
    for thisComponent in text_0Components:
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
    
    # --- Run Routine "text_0" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text0* updates
        
        # if text0 is starting this frame...
        if text0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text0.frameNStart = frameN  # exact frame index
            text0.tStart = t  # local t and not account for scr refresh
            text0.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text0, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text0.started')
            # update status
            text0.status = STARTED
            text0.setAutoDraw(True)
        
        # if text0 is active this frame...
        if text0.status == STARTED:
            # update params
            pass
        
        # *text0_key_resp* updates
        waitOnFlip = False
        
        # if text0_key_resp is starting this frame...
        if text0_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text0_key_resp.frameNStart = frameN  # exact frame index
            text0_key_resp.tStart = t  # local t and not account for scr refresh
            text0_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text0_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text0_key_resp.started')
            # update status
            text0_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(text0_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(text0_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if text0_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = text0_key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _text0_key_resp_allKeys.extend(theseKeys)
            if len(_text0_key_resp_allKeys):
                text0_key_resp.keys = _text0_key_resp_allKeys[-1].name  # just the last key pressed
                text0_key_resp.rt = _text0_key_resp_allKeys[-1].rt
                text0_key_resp.duration = _text0_key_resp_allKeys[-1].duration
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
        for thisComponent in text_0Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "text_0" ---
    for thisComponent in text_0Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('text_0.stopped', globalClock.getTime(format='float'))
    # check responses
    if text0_key_resp.keys in ['', [], None]:  # No response was made
        text0_key_resp.keys = None
    thisExp.addData('text0_key_resp.keys',text0_key_resp.keys)
    if text0_key_resp.keys != None:  # we had a response
        thisExp.addData('text0_key_resp.rt', text0_key_resp.rt)
        thisExp.addData('text0_key_resp.duration', text0_key_resp.duration)
    thisExp.nextEntry()
    # the Routine "text_0" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    training_trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='training_trials')
    thisExp.addLoop(training_trials)  # add the loop to the experiment
    thisTraining_trial = training_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTraining_trial.rgb)
    if thisTraining_trial != None:
        for paramName in thisTraining_trial:
            globals()[paramName] = thisTraining_trial[paramName]
    
    for thisTraining_trial in training_trials:
        currentLoop = training_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTraining_trial.rgb)
        if thisTraining_trial != None:
            for paramName in thisTraining_trial:
                globals()[paramName] = thisTraining_trial[paramName]
        
        # --- Prepare to start Routine "fixation_training" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('fixation_training.started', globalClock.getTime(format='float'))
        # keep track of which components have finished
        fixation_trainingComponents = [fixation0]
        for thisComponent in fixation_trainingComponents:
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
        
        # --- Run Routine "fixation_training" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation0* updates
            
            # if fixation0 is starting this frame...
            if fixation0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation0.frameNStart = frameN  # exact frame index
                fixation0.tStart = t  # local t and not account for scr refresh
                fixation0.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation0, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation0.started')
                # update status
                fixation0.status = STARTED
                fixation0.setAutoDraw(True)
            
            # if fixation0 is active this frame...
            if fixation0.status == STARTED:
                # update params
                pass
            
            # if fixation0 is stopping this frame...
            if fixation0.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation0.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation0.tStop = t  # not accounting for scr refresh
                    fixation0.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation0.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation0.stopped')
                    # update status
                    fixation0.status = FINISHED
                    fixation0.setAutoDraw(False)
            
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
            for thisComponent in fixation_trainingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation_training" ---
        for thisComponent in fixation_trainingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('fixation_training.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "main_training" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('main_training.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from training_code
        ## Begin Routine
        #
        ## Get the current trial
        leftimage_0 = trials0[current_trial0][0]
        rightimage_0 = trials0[current_trial0][1]
        #
        ## Define positions
        #left_pos = (-200, 0)  # Example position for left image
        #right_pos = (200, 0)  # Example position for right image
        #
        ## Draw left image
        #images[int(left_image.split('/')[1][0]) - 1].pos = left_pos
        #images[int(left_image.split('/')[1][0]) - 1].draw()
        #
        ## Draw right image
        #images[int(right_image.split('/')[1][0]) - 1].pos = right_pos
        #images[int(right_image.split('/')[1][0]) - 1].draw()
        #
        ## Flip the window to display images
        #win.flip()
        #
        ## Wait for a key press (you can replace this with your trial timing)
        #event.waitKeys()
        #
        ## Clear the screen for the next trial
        #win.flip()
        #
        ## Increment trial index
        current_trial0 += 1
        #
        #
        #
        #
        #
        ## Main loop
        #for trial in range(len(image_stims)):
        #    image_stims[trial].draw()  # Draw the image
        
        left_image_0.setImage(leftimage_0)
        right_image_0.setImage(rightimage_0)
        key_resp_0.keys = []
        key_resp_0.rt = []
        _key_resp_0_allKeys = []
        # Run 'Begin Routine' code from code_0
        sample_A1 = -1
        sample_B = -1
        sample_A2 = -1
        sample_C = -1
        
        # to check the sample be in range mean+-3sd
        while sample_A1 < 0 or sample_A1 > 100:
            sample_A1 = np.random.normal(64, 13, 1)[0]  # mean, std_dev, num_samples
        
        while sample_B < 0 or sample_A1 > 100:
            sample_B = np.random.normal(54, 13, 1)[0]  # mean, std_dev, num_samples
        
        while sample_A2 < 0 or sample_A1 > 100:
            sample_A2 = np.random.normal(64, 13, 1)[0]  # mean, std_dev, num_samples
        
        while sample_C < 0 or sample_A1 > 100:
            sample_C = np.random.normal(44, 13, 1)[0]  # mean, std_dev, num_samples
        
        
        #
        #
        ## Hide the text component initially
        #text_no_resp.setAutoDraw(False)
        #
        ## Record the start time of the routine
        #routineStartTime = t
        #
        ## Example boolean condition (replace this with your actual condition)
        #no_response = False  # Initialize with your condition value
        
        
        no_response = False
        
        routineStartTime = t
        left_learning_reward_0.reset()
        left_learning_reward_0.setText('')
        right_learning_reward_0.reset()
        right_learning_reward_0.setText('')
        # keep track of which components have finished
        main_trainingComponents = [left_image_0, right_image_0, key_resp_0, polygon_0, left_learning_reward_0, right_learning_reward_0, text_no_resp_0]
        for thisComponent in main_trainingComponents:
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
        
        # --- Run Routine "main_training" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *left_image_0* updates
            
            # if left_image_0 is starting this frame...
            if left_image_0.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                left_image_0.frameNStart = frameN  # exact frame index
                left_image_0.tStart = t  # local t and not account for scr refresh
                left_image_0.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_image_0, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'left_image_0.started')
                # update status
                left_image_0.status = STARTED
                left_image_0.setAutoDraw(True)
            
            # if left_image_0 is active this frame...
            if left_image_0.status == STARTED:
                # update params
                pass
            
            # if left_image_0 is stopping this frame...
            if left_image_0.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > left_image_0.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    left_image_0.tStop = t  # not accounting for scr refresh
                    left_image_0.tStopRefresh = tThisFlipGlobal  # on global time
                    left_image_0.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'left_image_0.stopped')
                    # update status
                    left_image_0.status = FINISHED
                    left_image_0.setAutoDraw(False)
            
            # *right_image_0* updates
            
            # if right_image_0 is starting this frame...
            if right_image_0.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                right_image_0.frameNStart = frameN  # exact frame index
                right_image_0.tStart = t  # local t and not account for scr refresh
                right_image_0.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_image_0, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'right_image_0.started')
                # update status
                right_image_0.status = STARTED
                right_image_0.setAutoDraw(True)
            
            # if right_image_0 is active this frame...
            if right_image_0.status == STARTED:
                # update params
                pass
            
            # if right_image_0 is stopping this frame...
            if right_image_0.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > right_image_0.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    right_image_0.tStop = t  # not accounting for scr refresh
                    right_image_0.tStopRefresh = tThisFlipGlobal  # on global time
                    right_image_0.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'right_image_0.stopped')
                    # update status
                    right_image_0.status = FINISHED
                    right_image_0.setAutoDraw(False)
            
            # *key_resp_0* updates
            waitOnFlip = False
            
            # if key_resp_0 is starting this frame...
            if key_resp_0.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_0.frameNStart = frameN  # exact frame index
                key_resp_0.tStart = t  # local t and not account for scr refresh
                key_resp_0.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_0, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_0.started')
                # update status
                key_resp_0.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_0.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_0.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_0 is stopping this frame...
            if key_resp_0.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_0.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_0.tStop = t  # not accounting for scr refresh
                    key_resp_0.tStopRefresh = tThisFlipGlobal  # on global time
                    key_resp_0.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_0.stopped')
                    # update status
                    key_resp_0.status = FINISHED
                    key_resp_0.status = FINISHED
            if key_resp_0.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_0.getKeys(keyList=['right','left'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_0_allKeys.extend(theseKeys)
                if len(_key_resp_0_allKeys):
                    key_resp_0.keys = _key_resp_0_allKeys[-1].name  # just the last key pressed
                    key_resp_0.rt = _key_resp_0_allKeys[-1].rt
                    key_resp_0.duration = _key_resp_0_allKeys[-1].duration
            # Run 'Each Frame' code from code_0
            if trials0[current_trial0-1][0] == "1-1.jpg":
            #    left_learning_reward.text = "1"
            #    right_learning_reward.text = "2"
            
                # A1 - left
                reward_A1 = int(round(sample_A1))
                # check the learning type - complete(1) or partial(2)
                if l_type=='1':
                    com_par_time=1
                    if key_resp_0.keys == 'left':
                        # Update the text component with the generated reward
                        left_learning_reward_0.text = f'Reward: {reward_A1}'
                    elif key_resp_0.keys == 'right':
                        # Update the text component with the generated reward
                        left_learning_reward_0.text = ''
                elif l_type=='2':
                    com_par_time=0.5
                    if key_resp_0.keys == 'left':
                        # Update the text component with the generated reward
                        left_learning_reward_0.text = f'Reward: {reward_A1}'
                    elif key_resp_0.keys == 'right':
                        # Update the text component with the generated reward
                        left_learning_reward_0.text = ''
            
                # B - right
                reward_B = int(round(sample_B))
                # check the learning type - complete(1) or partial(2)
                if l_type=='1':
                    com_par_time=1
                    if key_resp_0.keys == 'right':
                        # Update the text component with the generated reward
                        right_learning_reward_0.text = f'Reward: {reward_B}'
                    elif key_resp_0.keys == 'left':
                        # Update the text component with the generated reward
                        right_learning_reward_0.text = ''
                elif l_type=='2':
                    com_par_time=0.5
                    if key_resp_0.keys == 'right':
                        # Update the text component with the generated reward
                        right_learning_reward_0.text = f'Reward: {reward_B}'
                    elif key_resp_0.keys == 'left':
                        # Update the text component with the generated reward
                        right_learning_reward_0.text = ''
            
            elif trials0[current_trial0-1][0] == "1-2.jpg":
            #    left_learning_reward.text = "2"
            #    right_learning_reward.text = "1"
            
                # B - left
                reward_B = int(round(sample_B))
                # check the learning type - complete(1) or partial(2)
                if l_type=='1':
                    com_par_time=1
                    if key_resp_0.keys == 'left':
                        # Update the text component with the generated reward
                        left_learning_reward_0.text = f'Reward: {reward_B}'
                    elif key_resp_0.keys == 'right':
                        # Update the text component with the generated reward
                        left_learning_reward_0.text = ''
                elif l_type=='2':
                    com_par_time=0.5
                    if key_resp_0.keys == 'left':
                        # Update the text component with the generated reward
                        left_learning_reward_0.text = f'Reward: {reward_B}'
                    elif key_resp_0.keys == 'right':
                        # Update the text component with the generated reward
                        left_learning_reward_0.text = ''
                
                # A1 - right
                reward_A1 = int(round(sample_A1))
                # check the learning type - complete(1) or partial(2)
                if l_type=='1':
                    com_par_time=1
                    if key_resp_0.keys == 'right':
                        # Update the text component with the generated reward
                        right_learning_reward_0.text = f'Reward: {reward_A1}'
                    elif key_resp_0.keys == 'left':
                        # Update the text component with the generated reward
                        right_learning_reward_0.text = ''
                elif l_type=='2':
                    com_par_time=0.5
                    if key_resp_0.keys == 'right':
                        # Update the text component with the generated reward
                        right_learning_reward_0.text = f'Reward: {reward_A1}'
                    elif key_resp_0.keys == 'left':
                        # Update the text component with the generated reward
                        right_learning_reward_0.text = ''
            
            elif trials0[current_trial0-1][0] == "1-3.jpg":
            #    left_learning_reward.text = "3"
            #    right_learning_reward.text = "4"
                
                # A2 - left
                reward_A2 = int(round(sample_A2))
                # check the learning type - complete(1) or partial(2)
                if l_type=='1':
                    com_par_time=1
                    if key_resp_0.keys == 'left':
                        # Update the text component with the generated reward
                        left_learning_reward_0.text = f'Reward: {reward_A2}'
                    elif key_resp_0.keys == 'right':
                        # Update the text component with the generated reward
                        left_learning_reward_0.text = ''
                elif l_type=='2':
                    com_par_time=0.5
                    if key_resp_0.keys == 'left':
                        # Update the text component with the generated reward
                        left_learning_reward_0.text = f'Reward: {reward_A2}'
                    elif key_resp_0.keys == 'right':
                        # Update the text component with the generated reward
                        left_learning_reward_0.text = ''
            
                # C - right
                reward_C = int(round(sample_C))
                # check the learning type - complete(1) or partial(2)
                if l_type=='1':
                    com_par_time=1
                    if key_resp_0.keys == 'right':
                        # Update the text component with the generated reward
                        right_learning_reward_0.text = f'Reward: {reward_C}'
                    elif key_resp_0.keys == 'left':
                        # Update the text component with the generated reward
                        right_learning_reward_0.text = ''
                elif l_type=='2':
                    com_par_time=0.5
                    if key_resp_0.keys == 'right':
                        # Update the text component with the generated reward
                        right_learning_reward_0.text = f'Reward: {reward_C}'
                    elif key_resp_0.keys == 'left':
                        # Update the text component with the generated reward
                        right_learning_reward_0.text = ''
            
            elif trials0[current_trial0-1][0] == "1-4.jpg":
            #    left_learning_reward.text = "4"
            #    right_learning_reward.text = "3"
            
                # C - left
                reward_C = int(round(sample_C))
                # check the learning type - complete(1) or partial(2)
                if l_type=='1':
                    com_par_time=1
                    if key_resp_0.keys == 'left':
                        # Update the text component with the generated reward
                        left_learning_reward_0.text = f'Reward: {reward_C}'
                    elif key_resp_0.keys == 'right':
                        # Update the text component with the generated reward
                        left_learning_reward_0.text = ''
                elif l_type=='2':
                    com_par_time=0.5
                    if key_resp_0.keys == 'left':
                        # Update the text component with the generated reward
                        left_learning_reward_0.text = f'Reward: {reward_C}'
                    elif key_resp_0.keys == 'right':
                        # Update the text component with the generated reward
                        left_learning_reward_0.text = ''
            
                # A2 - right
                reward_A2 = int(round(sample_A2))
                # check the learning type - complete(1) or partial(2)
                if l_type=='1':
                    com_par_time=1
                    if key_resp_0.keys == 'right':
                        # Update the text component with the generated reward
                        right_learning_reward_0.text = f'Reward: {reward_A2}'
                    elif key_resp_0.keys == 'left':
                        # Update the text component with the generated reward
                        right_learning_reward_0.text = ''
                elif l_type=='2':
                    com_par_time=0.5
                    if key_resp_0.keys == 'right':
                        # Update the text component with the generated reward
                        right_learning_reward_0.text = f'Reward: {reward_A2}'
                    elif key_resp_0.keys == 'left':
                        # Update the text component with the generated reward
                        right_learning_reward_0.text = ''
            
            # Check if a key has been pressed
            if key_resp_0.keys == 'left':
                pos_k0=[-0.5,0]
                if t >= routineStartTime + 5.0:
                    continueRoutine = False
            #    no_response = False
            elif key_resp_0.keys == 'right':  # If any key other than 'right' is pressed
                pos_k0=[0.5,0]
                if t >= routineStartTime + 5.0:
                    continueRoutine = False
            #    no_response = False
            else:  # If any key other than 'right' is pressed
                pos_k0=[1.5,0]
                if t >= routineStartTime + 5.0 and t <= routineStartTime + 6.0:
                    no_response = True
            #    no_response = True
            
            
            
            #
            #
            ## Check if 5 seconds have passed
            #if t >= routineStartTime + 5.0 and t <= routineStartTime + 6.0:
            #    # Check the boolean condition
            #    if no_response:
            #        text_no_resp.setAutoDraw(True)  # Show the text component
            #    else:
            #        text_no_resp.setAutoDraw(False)  # Hide the text component
            #else:
            #    # Ensure the text component is hidden before 5 seconds
            #    text_no_resp.setAutoDraw(False)
            #
            
            # *polygon_0* updates
            
            # if polygon_0 is starting this frame...
            if polygon_0.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                polygon_0.frameNStart = frameN  # exact frame index
                polygon_0.tStart = t  # local t and not account for scr refresh
                polygon_0.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_0, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_0.started')
                # update status
                polygon_0.status = STARTED
                polygon_0.setAutoDraw(True)
            
            # if polygon_0 is active this frame...
            if polygon_0.status == STARTED:
                # update params
                polygon_0.setPos(pos_k0, log=False)
            
            # if polygon_0 is stopping this frame...
            if polygon_0.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_0.tStartRefresh + com_par_time-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_0.tStop = t  # not accounting for scr refresh
                    polygon_0.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon_0.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_0.stopped')
                    # update status
                    polygon_0.status = FINISHED
                    polygon_0.setAutoDraw(False)
            
            # *left_learning_reward_0* updates
            
            # if left_learning_reward_0 is starting this frame...
            if left_learning_reward_0.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                left_learning_reward_0.frameNStart = frameN  # exact frame index
                left_learning_reward_0.tStart = t  # local t and not account for scr refresh
                left_learning_reward_0.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_learning_reward_0, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'left_learning_reward_0.started')
                # update status
                left_learning_reward_0.status = STARTED
                left_learning_reward_0.setAutoDraw(True)
            
            # if left_learning_reward_0 is active this frame...
            if left_learning_reward_0.status == STARTED:
                # update params
                pass
            
            # if left_learning_reward_0 is stopping this frame...
            if left_learning_reward_0.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > left_learning_reward_0.tStartRefresh + com_par_time-frameTolerance:
                    # keep track of stop time/frame for later
                    left_learning_reward_0.tStop = t  # not accounting for scr refresh
                    left_learning_reward_0.tStopRefresh = tThisFlipGlobal  # on global time
                    left_learning_reward_0.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'left_learning_reward_0.stopped')
                    # update status
                    left_learning_reward_0.status = FINISHED
                    left_learning_reward_0.setAutoDraw(False)
            
            # *right_learning_reward_0* updates
            
            # if right_learning_reward_0 is starting this frame...
            if right_learning_reward_0.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                right_learning_reward_0.frameNStart = frameN  # exact frame index
                right_learning_reward_0.tStart = t  # local t and not account for scr refresh
                right_learning_reward_0.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_learning_reward_0, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'right_learning_reward_0.started')
                # update status
                right_learning_reward_0.status = STARTED
                right_learning_reward_0.setAutoDraw(True)
            
            # if right_learning_reward_0 is active this frame...
            if right_learning_reward_0.status == STARTED:
                # update params
                pass
            
            # if right_learning_reward_0 is stopping this frame...
            if right_learning_reward_0.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > right_learning_reward_0.tStartRefresh + com_par_time-frameTolerance:
                    # keep track of stop time/frame for later
                    right_learning_reward_0.tStop = t  # not accounting for scr refresh
                    right_learning_reward_0.tStopRefresh = tThisFlipGlobal  # on global time
                    right_learning_reward_0.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'right_learning_reward_0.stopped')
                    # update status
                    right_learning_reward_0.status = FINISHED
                    right_learning_reward_0.setAutoDraw(False)
            
            # *text_no_resp_0* updates
            
            # if text_no_resp_0 is starting this frame...
            if text_no_resp_0.status == NOT_STARTED and no_response:
                # keep track of start time/frame for later
                text_no_resp_0.frameNStart = frameN  # exact frame index
                text_no_resp_0.tStart = t  # local t and not account for scr refresh
                text_no_resp_0.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_no_resp_0, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_no_resp_0.started')
                # update status
                text_no_resp_0.status = STARTED
                text_no_resp_0.setAutoDraw(True)
            
            # if text_no_resp_0 is active this frame...
            if text_no_resp_0.status == STARTED:
                # update params
                text_no_resp_0.setText('پاسخی دریافت نشد.', log=False)
            
            # if text_no_resp_0 is stopping this frame...
            if text_no_resp_0.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_no_resp_0.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_no_resp_0.tStop = t  # not accounting for scr refresh
                    text_no_resp_0.tStopRefresh = tThisFlipGlobal  # on global time
                    text_no_resp_0.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_no_resp_0.stopped')
                    # update status
                    text_no_resp_0.status = FINISHED
                    text_no_resp_0.setAutoDraw(False)
            
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
            for thisComponent in main_trainingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "main_training" ---
        for thisComponent in main_trainingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('main_training.stopped', globalClock.getTime(format='float'))
        # check responses
        if key_resp_0.keys in ['', [], None]:  # No response was made
            key_resp_0.keys = None
        training_trials.addData('key_resp_0.keys',key_resp_0.keys)
        if key_resp_0.keys != None:  # we had a response
            training_trials.addData('key_resp_0.rt', key_resp_0.rt)
            training_trials.addData('key_resp_0.duration', key_resp_0.duration)
        # Run 'End Routine' code from code_0
        #if no_response == False:
        #    continueRoutine=False
        # the Routine "main_training" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'training_trials'
    
    
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
    learning_trials = data.TrialHandler(nReps=2.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='learning_trials')
    thisExp.addLoop(learning_trials)  # add the loop to the experiment
    thisLearning_trial = learning_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLearning_trial.rgb)
    if thisLearning_trial != None:
        for paramName in thisLearning_trial:
            globals()[paramName] = thisLearning_trial[paramName]
    
    for thisLearning_trial in learning_trials:
        currentLoop = learning_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisLearning_trial.rgb)
        if thisLearning_trial != None:
            for paramName in thisLearning_trial:
                globals()[paramName] = thisLearning_trial[paramName]
        
        # --- Prepare to start Routine "fixation_learning" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('fixation_learning.started', globalClock.getTime(format='float'))
        # keep track of which components have finished
        fixation_learningComponents = [fixation1]
        for thisComponent in fixation_learningComponents:
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
        
        # --- Run Routine "fixation_learning" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
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
                if tThisFlipGlobal > fixation1.tStartRefresh + 1.0-frameTolerance:
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
            for thisComponent in fixation_learningComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation_learning" ---
        for thisComponent in fixation_learningComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('fixation_learning.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "main_learning" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('main_learning.started', globalClock.getTime(format='float'))
        win.color = [1.0000, 1.0000, 1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        # Run 'Begin Routine' code from learning_code
        ## Begin Routine
        #
        ## Get the current trial
        leftimage = trials[current_trial][0]
        rightimage = trials[current_trial][1]
        #
        ## Define positions
        #left_pos = (-200, 0)  # Example position for left image
        #right_pos = (200, 0)  # Example position for right image
        #
        ## Draw left image
        #images[int(left_image.split('/')[1][0]) - 1].pos = left_pos
        #images[int(left_image.split('/')[1][0]) - 1].draw()
        #
        ## Draw right image
        #images[int(right_image.split('/')[1][0]) - 1].pos = right_pos
        #images[int(right_image.split('/')[1][0]) - 1].draw()
        #
        ## Flip the window to display images
        #win.flip()
        #
        ## Wait for a key press (you can replace this with your trial timing)
        #event.waitKeys()
        #
        ## Clear the screen for the next trial
        #win.flip()
        #
        ## Increment trial index
        current_trial += 1
        #
        #
        #
        #
        #
        ## Main loop
        #for trial in range(len(image_stims)):
        #    image_stims[trial].draw()  # Draw the image
        
        left_image.setImage(leftimage)
        right_image.setImage(rightimage)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # Run 'Begin Routine' code from code
        sample_A1 = -1
        sample_B = -1
        sample_A2 = -1
        sample_C = -1
        
        # to check the sample be in range mean+-3sd
        while sample_A1 < 0 or sample_A1 > 100:
            sample_A1 = np.random.normal(64, 13, 1)[0]  # mean, std_dev, num_samples
        
        while sample_B < 0 or sample_A1 > 100:
            sample_B = np.random.normal(54, 13, 1)[0]  # mean, std_dev, num_samples
        
        while sample_A2 < 0 or sample_A1 > 100:
            sample_A2 = np.random.normal(64, 13, 1)[0]  # mean, std_dev, num_samples
        
        while sample_C < 0 or sample_A1 > 100:
            sample_C = np.random.normal(44, 13, 1)[0]  # mean, std_dev, num_samples
        
        
        #
        #
        ## Hide the text component initially
        #text_no_resp.setAutoDraw(False)
        #
        ## Record the start time of the routine
        #routineStartTime = t
        #
        ## Example boolean condition (replace this with your actual condition)
        #no_response = False  # Initialize with your condition value
        
        
        no_response = False
        
        routineStartTime = t
        left_learning_reward.reset()
        left_learning_reward.setText('')
        right_learning_reward.reset()
        right_learning_reward.setText('')
        # keep track of which components have finished
        main_learningComponents = [left_image, right_image, key_resp, polygon, left_learning_reward, right_learning_reward, text_no_resp]
        for thisComponent in main_learningComponents:
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
        
        # --- Run Routine "main_learning" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *left_image* updates
            
            # if left_image is starting this frame...
            if left_image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                left_image.frameNStart = frameN  # exact frame index
                left_image.tStart = t  # local t and not account for scr refresh
                left_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'left_image.started')
                # update status
                left_image.status = STARTED
                left_image.setAutoDraw(True)
            
            # if left_image is active this frame...
            if left_image.status == STARTED:
                # update params
                pass
            
            # if left_image is stopping this frame...
            if left_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > left_image.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    left_image.tStop = t  # not accounting for scr refresh
                    left_image.tStopRefresh = tThisFlipGlobal  # on global time
                    left_image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'left_image.stopped')
                    # update status
                    left_image.status = FINISHED
                    left_image.setAutoDraw(False)
            
            # *right_image* updates
            
            # if right_image is starting this frame...
            if right_image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                right_image.frameNStart = frameN  # exact frame index
                right_image.tStart = t  # local t and not account for scr refresh
                right_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'right_image.started')
                # update status
                right_image.status = STARTED
                right_image.setAutoDraw(True)
            
            # if right_image is active this frame...
            if right_image.status == STARTED:
                # update params
                pass
            
            # if right_image is stopping this frame...
            if right_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > right_image.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    right_image.tStop = t  # not accounting for scr refresh
                    right_image.tStopRefresh = tThisFlipGlobal  # on global time
                    right_image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'right_image.stopped')
                    # update status
                    right_image.status = FINISHED
                    right_image.setAutoDraw(False)
            
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
            # Run 'Each Frame' code from code
            if trials[current_trial-1][0] == "1.jpg":
            #    left_learning_reward.text = "1"
            #    right_learning_reward.text = "2"
            
                # A1 - left
                reward_A1 = int(round(sample_A1))
                # store this reward in the PsychoPy data file or use it in your experiment
                thisExp.addData('reward_A1', reward_A1)  # Save it to the data file
                # check the learning type - complete(1) or partial(2)
                if l_type=='1':
                    com_par_time=1
                    if key_resp.keys == 'left':
                        # Update the text component with the generated reward
                        left_learning_reward.text = f'Reward: {reward_A1}'
                        thisExp.addData('gain_reward', reward_A1)  # Save it to the data file
                        rewards_array.append(reward_A1)
                    elif key_resp.keys == 'right':
                        # Update the text component with the generated reward
                        left_learning_reward.text = ''
                elif l_type=='2':
                    com_par_time=0.5
                    if key_resp.keys == 'left':
                        # Update the text component with the generated reward
                        left_learning_reward.text = f'Reward: {reward_A1}'
                        thisExp.addData('gain_reward', reward_A1)  # Save it to the data file
                        rewards_array.append(reward_A1)
                    elif key_resp.keys == 'right':
                        # Update the text component with the generated reward
                        left_learning_reward.text = ''
            
                # B - right
                reward_B = int(round(sample_B))
                # store this reward in the PsychoPy data file or use it in your experiment
                thisExp.addData('reward_B', reward_B)  # Save it to the data file
                # check the learning type - complete(1) or partial(2)
                if l_type=='1':
                    com_par_time=1
                    if key_resp.keys == 'right':
                        # Update the text component with the generated reward
                        right_learning_reward.text = f'Reward: {reward_B}'
                        thisExp.addData('gain_reward', reward_B)  # Save it to the data file
                        rewards_array.append(reward_B)
                    elif key_resp.keys == 'left':
                        # Update the text component with the generated reward
                        right_learning_reward.text = ''
                elif l_type=='2':
                    com_par_time=0.5
                    if key_resp.keys == 'right':
                        # Update the text component with the generated reward
                        right_learning_reward.text = f'Reward: {reward_B}'
                        thisExp.addData('gain_reward', reward_B)  # Save it to the data file
                        rewards_array.append(reward_B)
                    elif key_resp.keys == 'left':
                        # Update the text component with the generated reward
                        right_learning_reward.text = ''
            
            elif trials[current_trial-1][0] == "2.jpg":
            #    left_learning_reward.text = "2"
            #    right_learning_reward.text = "1"
            
                # B - left
                reward_B = int(round(sample_B))
                # store this reward in the PsychoPy data file or use it in your experiment
                thisExp.addData('reward_B', reward_B)  # Save it to the data file
                # check the learning type - complete(1) or partial(2)
                if l_type=='1':
                    com_par_time=1
                    if key_resp.keys == 'left':
                        # Update the text component with the generated reward
                        left_learning_reward.text = f'Reward: {reward_B}'
                        thisExp.addData('gain_reward', reward_B)  # Save it to the data file
                        rewards_array.append(reward_B)
                    elif key_resp.keys == 'right':
                        # Update the text component with the generated reward
                        left_learning_reward.text = ''
                elif l_type=='2':
                    com_par_time=0.5
                    if key_resp.keys == 'left':
                        # Update the text component with the generated reward
                        left_learning_reward.text = f'Reward: {reward_B}'
                        thisExp.addData('gain_reward', reward_B)  # Save it to the data file
                        rewards_array.append(reward_B)
                    elif key_resp.keys == 'right':
                        # Update the text component with the generated reward
                        left_learning_reward.text = ''
                
                # A1 - right
                reward_A1 = int(round(sample_A1))
                # store this reward in the PsychoPy data file or use it in your experiment
                thisExp.addData('reward_A1', reward_A1)  # Save it to the data file
                # check the learning type - complete(1) or partial(2)
                if l_type=='1':
                    com_par_time=1
                    if key_resp.keys == 'right':
                        # Update the text component with the generated reward
                        right_learning_reward.text = f'Reward: {reward_A1}'
                        thisExp.addData('gain_reward', reward_A1)  # Save it to the data file
                        rewards_array.append(reward_A1)
                    elif key_resp.keys == 'left':
                        # Update the text component with the generated reward
                        right_learning_reward.text = ''
                elif l_type=='2':
                    com_par_time=0.5
                    if key_resp.keys == 'right':
                        # Update the text component with the generated reward
                        right_learning_reward.text = f'Reward: {reward_A1}'
                        thisExp.addData('gain_reward', reward_A1)  # Save it to the data file
                        rewards_array.append(reward_A1)
                    elif key_resp.keys == 'left':
                        # Update the text component with the generated reward
                        right_learning_reward.text = ''
            
            elif trials[current_trial-1][0] == "3.jpg":
            #    left_learning_reward.text = "3"
            #    right_learning_reward.text = "4"
                
                # A2 - left
                reward_A2 = int(round(sample_A2))
                # store this reward in the PsychoPy data file or use it in your experiment
                thisExp.addData('reward_A2', reward_A2)  # Save it to the data file
                # check the learning type - complete(1) or partial(2)
                if l_type=='1':
                    com_par_time=1
                    if key_resp.keys == 'left':
                        # Update the text component with the generated reward
                        left_learning_reward.text = f'Reward: {reward_A2}'
                        thisExp.addData('gain_reward', reward_A2)  # Save it to the data file
                        rewards_array.append(reward_A2)
                    elif key_resp.keys == 'right':
                        # Update the text component with the generated reward
                        left_learning_reward.text = ''
                elif l_type=='2':
                    com_par_time=0.5
                    if key_resp.keys == 'left':
                        # Update the text component with the generated reward
                        left_learning_reward.text = f'Reward: {reward_A2}'
                        thisExp.addData('gain_reward', reward_A2)  # Save it to the data file
                        rewards_array.append(reward_A2)
                    elif key_resp.keys == 'right':
                        # Update the text component with the generated reward
                        left_learning_reward.text = ''
            
                # C - right
                reward_C = int(round(sample_C))
                # store this reward in the PsychoPy data file or use it in your experiment
                thisExp.addData('reward_C', reward_C)  # Save it to the data file
                # check the learning type - complete(1) or partial(2)
                if l_type=='1':
                    com_par_time=1
                    if key_resp.keys == 'right':
                        # Update the text component with the generated reward
                        right_learning_reward.text = f'Reward: {reward_C}'
                        thisExp.addData('gain_reward', reward_C)  # Save it to the data file
                        rewards_array.append(reward_C)
                    elif key_resp.keys == 'left':
                        # Update the text component with the generated reward
                        right_learning_reward.text = ''
                elif l_type=='2':
                    com_par_time=0.5
                    if key_resp.keys == 'right':
                        # Update the text component with the generated reward
                        right_learning_reward.text = f'Reward: {reward_C}'
                        thisExp.addData('gain_reward', reward_C)  # Save it to the data file
                        rewards_array.append(reward_C)
                    elif key_resp.keys == 'left':
                        # Update the text component with the generated reward
                        right_learning_reward.text = ''
            
            elif trials[current_trial-1][0] == "4.jpg":
            #    left_learning_reward.text = "4"
            #    right_learning_reward.text = "3"
            
                # C - left
                reward_C = int(round(sample_C))
                # store this reward in the PsychoPy data file or use it in your experiment
                thisExp.addData('reward_C', reward_C)  # Save it to the data file
                # check the learning type - complete(1) or partial(2)
                if l_type=='1':
                    com_par_time=1
                    if key_resp.keys == 'left':
                        # Update the text component with the generated reward
                        left_learning_reward.text = f'Reward: {reward_C}'
                        thisExp.addData('gain_reward', reward_C)  # Save it to the data file
                        rewards_array.append(reward_C)
                    elif key_resp.keys == 'right':
                        # Update the text component with the generated reward
                        left_learning_reward.text = ''
                elif l_type=='2':
                    com_par_time=0.5
                    if key_resp.keys == 'left':
                        # Update the text component with the generated reward
                        left_learning_reward.text = f'Reward: {reward_C}'
                        thisExp.addData('gain_reward', reward_C)  # Save it to the data file
                        rewards_array.append(reward_C)
                    elif key_resp.keys == 'right':
                        # Update the text component with the generated reward
                        left_learning_reward.text = ''
            
                # A2 - right
                reward_A2 = int(round(sample_A2))
                # store this reward in the PsychoPy data file or use it in your experiment
                thisExp.addData('reward_A2', reward_A2)  # Save it to the data file
                # check the learning type - complete(1) or partial(2)
                if l_type=='1':
                    com_par_time=1
                    if key_resp.keys == 'right':
                        # Update the text component with the generated reward
                        right_learning_reward.text = f'Reward: {reward_A2}'
                        thisExp.addData('gain_reward', reward_A2)  # Save it to the data file
                        rewards_array.append(reward_A2)
                    elif key_resp.keys == 'left':
                        # Update the text component with the generated reward
                        right_learning_reward.text = ''
                elif l_type=='2':
                    com_par_time=0.5
                    if key_resp.keys == 'right':
                        # Update the text component with the generated reward
                        right_learning_reward.text = f'Reward: {reward_A2}'
                        thisExp.addData('gain_reward', reward_A2)  # Save it to the data file
                        rewards_array.append(reward_A2)
                    elif key_resp.keys == 'left':
                        # Update the text component with the generated reward
                        right_learning_reward.text = ''
            
            # Check if a key has been pressed
            if key_resp.keys == 'left':
                pos_k=[-0.5,0]
                if t >= routineStartTime + 5.0:
                    continueRoutine = False
            #    no_response = False
            elif key_resp.keys == 'right':  # If any key other than 'right' is pressed
                pos_k=[0.5,0]
                if t >= routineStartTime + 5.0:
                    continueRoutine = False
            #    no_response = False
            else:  # If any key other than 'right' is pressed
                pos_k=[1.5,0]
                if t >= routineStartTime + 5.0 and t <= routineStartTime + 6.0:
                    no_response = True
            #    no_response = True
            
            
            
            #
            #
            ## Check if 5 seconds have passed
            #if t >= routineStartTime + 5.0 and t <= routineStartTime + 6.0:
            #    # Check the boolean condition
            #    if no_response:
            #        text_no_resp.setAutoDraw(True)  # Show the text component
            #    else:
            #        text_no_resp.setAutoDraw(False)  # Hide the text component
            #else:
            #    # Ensure the text component is hidden before 5 seconds
            #    text_no_resp.setAutoDraw(False)
            #
            
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
                if tThisFlipGlobal > polygon.tStartRefresh + com_par_time-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.stopped')
                    # update status
                    polygon.status = FINISHED
                    polygon.setAutoDraw(False)
            
            # *left_learning_reward* updates
            
            # if left_learning_reward is starting this frame...
            if left_learning_reward.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                left_learning_reward.frameNStart = frameN  # exact frame index
                left_learning_reward.tStart = t  # local t and not account for scr refresh
                left_learning_reward.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_learning_reward, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'left_learning_reward.started')
                # update status
                left_learning_reward.status = STARTED
                left_learning_reward.setAutoDraw(True)
            
            # if left_learning_reward is active this frame...
            if left_learning_reward.status == STARTED:
                # update params
                pass
            
            # if left_learning_reward is stopping this frame...
            if left_learning_reward.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > left_learning_reward.tStartRefresh + com_par_time-frameTolerance:
                    # keep track of stop time/frame for later
                    left_learning_reward.tStop = t  # not accounting for scr refresh
                    left_learning_reward.tStopRefresh = tThisFlipGlobal  # on global time
                    left_learning_reward.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'left_learning_reward.stopped')
                    # update status
                    left_learning_reward.status = FINISHED
                    left_learning_reward.setAutoDraw(False)
            
            # *right_learning_reward* updates
            
            # if right_learning_reward is starting this frame...
            if right_learning_reward.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                right_learning_reward.frameNStart = frameN  # exact frame index
                right_learning_reward.tStart = t  # local t and not account for scr refresh
                right_learning_reward.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_learning_reward, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'right_learning_reward.started')
                # update status
                right_learning_reward.status = STARTED
                right_learning_reward.setAutoDraw(True)
            
            # if right_learning_reward is active this frame...
            if right_learning_reward.status == STARTED:
                # update params
                pass
            
            # if right_learning_reward is stopping this frame...
            if right_learning_reward.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > right_learning_reward.tStartRefresh + com_par_time-frameTolerance:
                    # keep track of stop time/frame for later
                    right_learning_reward.tStop = t  # not accounting for scr refresh
                    right_learning_reward.tStopRefresh = tThisFlipGlobal  # on global time
                    right_learning_reward.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'right_learning_reward.stopped')
                    # update status
                    right_learning_reward.status = FINISHED
                    right_learning_reward.setAutoDraw(False)
            
            # *text_no_resp* updates
            
            # if text_no_resp is starting this frame...
            if text_no_resp.status == NOT_STARTED and no_response:
                # keep track of start time/frame for later
                text_no_resp.frameNStart = frameN  # exact frame index
                text_no_resp.tStart = t  # local t and not account for scr refresh
                text_no_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_no_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_no_resp.started')
                # update status
                text_no_resp.status = STARTED
                text_no_resp.setAutoDraw(True)
            
            # if text_no_resp is active this frame...
            if text_no_resp.status == STARTED:
                # update params
                text_no_resp.setText('پاسخی دریافت نشد.', log=False)
            
            # if text_no_resp is stopping this frame...
            if text_no_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_no_resp.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_no_resp.tStop = t  # not accounting for scr refresh
                    text_no_resp.tStopRefresh = tThisFlipGlobal  # on global time
                    text_no_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_no_resp.stopped')
                    # update status
                    text_no_resp.status = FINISHED
                    text_no_resp.setAutoDraw(False)
            
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
            for thisComponent in main_learningComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "main_learning" ---
        for thisComponent in main_learningComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('main_learning.stopped', globalClock.getTime(format='float'))
        setupWindow(expInfo=expInfo, win=win)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        learning_trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            learning_trials.addData('key_resp.rt', key_resp.rt)
            learning_trials.addData('key_resp.duration', key_resp.duration)
        # Run 'End Routine' code from code
        #if no_response == False:
        #    continueRoutine=False
        # the Routine "main_learning" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 2.0 repeats of 'learning_trials'
    
    
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
    transfer_trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='transfer_trials')
    thisExp.addLoop(transfer_trials)  # add the loop to the experiment
    thisTransfer_trial = transfer_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTransfer_trial.rgb)
    if thisTransfer_trial != None:
        for paramName in thisTransfer_trial:
            globals()[paramName] = thisTransfer_trial[paramName]
    
    for thisTransfer_trial in transfer_trials:
        currentLoop = transfer_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTransfer_trial.rgb)
        if thisTransfer_trial != None:
            for paramName in thisTransfer_trial:
                globals()[paramName] = thisTransfer_trial[paramName]
        
        # --- Prepare to start Routine "fixation_transfer" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('fixation_transfer.started', globalClock.getTime(format='float'))
        # keep track of which components have finished
        fixation_transferComponents = [fixation2]
        for thisComponent in fixation_transferComponents:
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
        
        # --- Run Routine "fixation_transfer" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation2* updates
            
            # if fixation2 is starting this frame...
            if fixation2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation2.frameNStart = frameN  # exact frame index
                fixation2.tStart = t  # local t and not account for scr refresh
                fixation2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2.started')
                # update status
                fixation2.status = STARTED
                fixation2.setAutoDraw(True)
            
            # if fixation2 is active this frame...
            if fixation2.status == STARTED:
                # update params
                pass
            
            # if fixation2 is stopping this frame...
            if fixation2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation2.tStop = t  # not accounting for scr refresh
                    fixation2.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation2.stopped')
                    # update status
                    fixation2.status = FINISHED
                    fixation2.setAutoDraw(False)
            
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
            for thisComponent in fixation_transferComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation_transfer" ---
        for thisComponent in fixation_transferComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('fixation_transfer.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "main_transfer" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('main_transfer.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from transfer_code
        ## Begin Routine
        #
        ## Get the current trial
        leftimage = trials_2[current_trial_2][0]
        rightimage = trials_2[current_trial_2][1]
        #
        ## Define positions
        #left_pos = (-200, 0)  # Example position for left image
        #right_pos = (200, 0)  # Example position for right image
        #
        ## Draw left image
        #images[int(left_image.split('/')[1][0]) - 1].pos = left_pos
        #images[int(left_image.split('/')[1][0]) - 1].draw()
        #
        ## Draw right image
        #images[int(right_image.split('/')[1][0]) - 1].pos = right_pos
        #images[int(right_image.split('/')[1][0]) - 1].draw()
        #
        ## Flip the window to display images
        #win.flip()
        #
        ## Wait for a key press (you can replace this with your trial timing)
        #event.waitKeys()
        #
        ## Clear the screen for the next trial
        #win.flip()
        #
        ## Increment trial index
        current_trial_2 += 1
        #
        #
        #
        #
        #
        ## Main loop
        #for trial in range(len(image_stims)):
        #    image_stims[trial].draw()  # Draw the image
        
        left_image_2.setImage(leftimage)
        right_image_2.setImage(rightimage)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # Run 'Begin Routine' code from code_2
        start_time = t
        end_time = 1000
        end_time_more = False
        
        # keep track of which components have finished
        main_transferComponents = [left_image_2, right_image_2, key_resp_2, polygon_2]
        for thisComponent in main_transferComponents:
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
        
        # --- Run Routine "main_transfer" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *left_image_2* updates
            
            # if left_image_2 is starting this frame...
            if left_image_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                left_image_2.frameNStart = frameN  # exact frame index
                left_image_2.tStart = t  # local t and not account for scr refresh
                left_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'left_image_2.started')
                # update status
                left_image_2.status = STARTED
                left_image_2.setAutoDraw(True)
            
            # if left_image_2 is active this frame...
            if left_image_2.status == STARTED:
                # update params
                pass
            
            # if left_image_2 is stopping this frame...
            if left_image_2.status == STARTED:
                if bool(end_time_more):
                    # keep track of stop time/frame for later
                    left_image_2.tStop = t  # not accounting for scr refresh
                    left_image_2.tStopRefresh = tThisFlipGlobal  # on global time
                    left_image_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'left_image_2.stopped')
                    # update status
                    left_image_2.status = FINISHED
                    left_image_2.setAutoDraw(False)
            
            # *right_image_2* updates
            
            # if right_image_2 is starting this frame...
            if right_image_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                right_image_2.frameNStart = frameN  # exact frame index
                right_image_2.tStart = t  # local t and not account for scr refresh
                right_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'right_image_2.started')
                # update status
                right_image_2.status = STARTED
                right_image_2.setAutoDraw(True)
            
            # if right_image_2 is active this frame...
            if right_image_2.status == STARTED:
                # update params
                pass
            
            # if right_image_2 is stopping this frame...
            if right_image_2.status == STARTED:
                if bool(end_time_more):
                    # keep track of stop time/frame for later
                    right_image_2.tStop = t  # not accounting for scr refresh
                    right_image_2.tStopRefresh = tThisFlipGlobal  # on global time
                    right_image_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'right_image_2.stopped')
                    # update status
                    right_image_2.status = FINISHED
                    right_image_2.setAutoDraw(False)
            
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
                # is it time to stop? (based on local clock)
                if tThisFlip > end_time-frameTolerance:
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
            # Run 'Each Frame' code from code_2
            # Check if a key has been pressed
            if key_resp_2.keys == 'left':
                pos_k_2=[-0.5,0]
                end_time = t
                core.wait(1.0)
                end_time_more = True
            elif key_resp_2.keys == 'right':
                pos_k_2=[0.5,0]
                end_time = t
                core.wait(1.0)
                end_time_more = True
            else:  # If any key other than 'right' is pressed
                pos_k_2=[1.5,0]
            
            # *polygon_2* updates
            
            # if polygon_2 is starting this frame...
            if polygon_2.status == NOT_STARTED and tThisFlip >= end_time-frameTolerance:
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
                polygon_2.setPos(pos_k_2, log=False)
            
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
            for thisComponent in main_transferComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "main_transfer" ---
        for thisComponent in main_transferComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('main_transfer.stopped', globalClock.getTime(format='float'))
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        transfer_trials.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            transfer_trials.addData('key_resp_2.rt', key_resp_2.rt)
            transfer_trials.addData('key_resp_2.duration', key_resp_2.duration)
        # the Routine "main_transfer" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "slider_transfer" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('slider_transfer.started', globalClock.getTime(format='float'))
        slider_trns.reset()
        # setup some python lists for storing info about the mouse_trns
        mouse_trns.x = []
        mouse_trns.y = []
        mouse_trns.leftButton = []
        mouse_trns.midButton = []
        mouse_trns.rightButton = []
        mouse_trns.time = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from code_3
        # Make sure the mouse cursor is visible
        win.mouseVisible = True
        
        # keep track of which components have finished
        slider_transferComponents = [slider_trns, mouse_trns]
        for thisComponent in slider_transferComponents:
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
        
        # --- Run Routine "slider_transfer" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *slider_trns* updates
            
            # if slider_trns is starting this frame...
            if slider_trns.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                slider_trns.frameNStart = frameN  # exact frame index
                slider_trns.tStart = t  # local t and not account for scr refresh
                slider_trns.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_trns, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_trns.started')
                # update status
                slider_trns.status = STARTED
                slider_trns.setAutoDraw(True)
            
            # if slider_trns is active this frame...
            if slider_trns.status == STARTED:
                # update params
                pass
            
            # Check slider_trns for response to end Routine
            if slider_trns.getRating() is not None and slider_trns.status == STARTED:
                continueRoutine = False
            # *mouse_trns* updates
            
            # if mouse_trns is starting this frame...
            if mouse_trns.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_trns.frameNStart = frameN  # exact frame index
                mouse_trns.tStart = t  # local t and not account for scr refresh
                mouse_trns.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_trns, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_trns.started', t)
                # update status
                mouse_trns.status = STARTED
                mouse_trns.mouseClock.reset()
                prevButtonState = mouse_trns.getPressed()  # if button is down already this ISN'T a new click
            if mouse_trns.status == STARTED:  # only update if started and not finished!
                buttons = mouse_trns.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        pass
                        x, y = mouse_trns.getPos()
                        mouse_trns.x.append(x)
                        mouse_trns.y.append(y)
                        buttons = mouse_trns.getPressed()
                        mouse_trns.leftButton.append(buttons[0])
                        mouse_trns.midButton.append(buttons[1])
                        mouse_trns.rightButton.append(buttons[2])
                        mouse_trns.time.append(mouse_trns.mouseClock.getTime())
            
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
            for thisComponent in slider_transferComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "slider_transfer" ---
        for thisComponent in slider_transferComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('slider_transfer.stopped', globalClock.getTime(format='float'))
        transfer_trials.addData('slider_trns.response', slider_trns.getRating())
        transfer_trials.addData('slider_trns.rt', slider_trns.getRT())
        # store data for transfer_trials (TrialHandler)
        transfer_trials.addData('mouse_trns.x', mouse_trns.x)
        transfer_trials.addData('mouse_trns.y', mouse_trns.y)
        transfer_trials.addData('mouse_trns.leftButton', mouse_trns.leftButton)
        transfer_trials.addData('mouse_trns.midButton', mouse_trns.midButton)
        transfer_trials.addData('mouse_trns.rightButton', mouse_trns.rightButton)
        transfer_trials.addData('mouse_trns.time', mouse_trns.time)
        # the Routine "slider_transfer" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'transfer_trials'
    
    
    # --- Prepare to start Routine "text_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('text_3.started', globalClock.getTime(format='float'))
    text3_key_resp.keys = []
    text3_key_resp.rt = []
    _text3_key_resp_allKeys = []
    # keep track of which components have finished
    text_3Components = [text3, text3_key_resp]
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
    if text3_key_resp.keys in ['', [], None]:  # No response was made
        text3_key_resp.keys = None
    thisExp.addData('text3_key_resp.keys',text3_key_resp.keys)
    if text3_key_resp.keys != None:  # we had a response
        thisExp.addData('text3_key_resp.rt', text3_key_resp.rt)
        thisExp.addData('text3_key_resp.duration', text3_key_resp.duration)
    thisExp.nextEntry()
    # the Routine "text_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    estimation_trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='estimation_trials')
    thisExp.addLoop(estimation_trials)  # add the loop to the experiment
    thisEstimation_trial = estimation_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEstimation_trial.rgb)
    if thisEstimation_trial != None:
        for paramName in thisEstimation_trial:
            globals()[paramName] = thisEstimation_trial[paramName]
    
    for thisEstimation_trial in estimation_trials:
        currentLoop = estimation_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisEstimation_trial.rgb)
        if thisEstimation_trial != None:
            for paramName in thisEstimation_trial:
                globals()[paramName] = thisEstimation_trial[paramName]
        
        # --- Prepare to start Routine "fixation_estimation" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('fixation_estimation.started', globalClock.getTime(format='float'))
        # keep track of which components have finished
        fixation_estimationComponents = [fixation3]
        for thisComponent in fixation_estimationComponents:
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
        
        # --- Run Routine "fixation_estimation" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation3* updates
            
            # if fixation3 is starting this frame...
            if fixation3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation3.frameNStart = frameN  # exact frame index
                fixation3.tStart = t  # local t and not account for scr refresh
                fixation3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation3.started')
                # update status
                fixation3.status = STARTED
                fixation3.setAutoDraw(True)
            
            # if fixation3 is active this frame...
            if fixation3.status == STARTED:
                # update params
                pass
            
            # if fixation3 is stopping this frame...
            if fixation3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation3.tStop = t  # not accounting for scr refresh
                    fixation3.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation3.stopped')
                    # update status
                    fixation3.status = FINISHED
                    fixation3.setAutoDraw(False)
            
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
            for thisComponent in fixation_estimationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation_estimation" ---
        for thisComponent in fixation_estimationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('fixation_estimation.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "main_estimation" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('main_estimation.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from estimation_code
        ## Begin Routine
        #
        ## Get the current trial
        image = trials_3[current_trial_3]
        #
        ## Define positions
        #left_pos = (-200, 0)  # Example position for left image
        #right_pos = (200, 0)  # Example position for right image
        #
        ## Draw left image
        #images[int(left_image.split('/')[1][0]) - 1].pos = left_pos
        #images[int(left_image.split('/')[1][0]) - 1].draw()
        #
        ## Draw right image
        #images[int(right_image.split('/')[1][0]) - 1].pos = right_pos
        #images[int(right_image.split('/')[1][0]) - 1].draw()
        #
        ## Flip the window to display images
        #win.flip()
        #
        ## Wait for a key press (you can replace this with your trial timing)
        #event.waitKeys()
        #
        ## Clear the screen for the next trial
        #win.flip()
        #
        ## Increment trial index
        current_trial_3 += 1
        #
        #
        #
        #
        #
        ## Main loop
        #for trial in range(len(image_stims)):
        #    image_stims[trial].draw()  # Draw the image
        
        image_3.setImage(image)
        slider_estm.reset()
        # setup some python lists for storing info about the mouse_estm
        mouse_estm.x = []
        mouse_estm.y = []
        mouse_estm.leftButton = []
        mouse_estm.midButton = []
        mouse_estm.rightButton = []
        mouse_estm.time = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from code_4
        # Make sure the mouse cursor is visible
        win.mouseVisible = True
        
        
        #
        ## Check if the mouse is pressed within the slider region
        #if mouse_estm.isPressedIn(slider_estm):
        #    continueRoutine = False  # End the routine if the slider is clicked
        #
        # keep track of which components have finished
        main_estimationComponents = [image_3, slider_estm, mouse_estm]
        for thisComponent in main_estimationComponents:
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
        
        # --- Run Routine "main_estimation" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_3* updates
            
            # if image_3 is starting this frame...
            if image_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_3.started')
                # update status
                image_3.status = STARTED
                image_3.setAutoDraw(True)
            
            # if image_3 is active this frame...
            if image_3.status == STARTED:
                # update params
                pass
            
            # *slider_estm* updates
            
            # if slider_estm is starting this frame...
            if slider_estm.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                slider_estm.frameNStart = frameN  # exact frame index
                slider_estm.tStart = t  # local t and not account for scr refresh
                slider_estm.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_estm, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_estm.started')
                # update status
                slider_estm.status = STARTED
                slider_estm.setAutoDraw(True)
            
            # if slider_estm is active this frame...
            if slider_estm.status == STARTED:
                # update params
                pass
            
            # Check slider_estm for response to end Routine
            if slider_estm.getRating() is not None and slider_estm.status == STARTED:
                continueRoutine = False
            # *mouse_estm* updates
            
            # if mouse_estm is starting this frame...
            if mouse_estm.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_estm.frameNStart = frameN  # exact frame index
                mouse_estm.tStart = t  # local t and not account for scr refresh
                mouse_estm.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_estm, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_estm.started', t)
                # update status
                mouse_estm.status = STARTED
                mouse_estm.mouseClock.reset()
                prevButtonState = mouse_estm.getPressed()  # if button is down already this ISN'T a new click
            if mouse_estm.status == STARTED:  # only update if started and not finished!
                buttons = mouse_estm.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        pass
                        x, y = mouse_estm.getPos()
                        mouse_estm.x.append(x)
                        mouse_estm.y.append(y)
                        buttons = mouse_estm.getPressed()
                        mouse_estm.leftButton.append(buttons[0])
                        mouse_estm.midButton.append(buttons[1])
                        mouse_estm.rightButton.append(buttons[2])
                        mouse_estm.time.append(mouse_estm.mouseClock.getTime())
            
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
            for thisComponent in main_estimationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "main_estimation" ---
        for thisComponent in main_estimationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('main_estimation.stopped', globalClock.getTime(format='float'))
        estimation_trials.addData('slider_estm.response', slider_estm.getRating())
        estimation_trials.addData('slider_estm.rt', slider_estm.getRT())
        # store data for estimation_trials (TrialHandler)
        estimation_trials.addData('mouse_estm.x', mouse_estm.x)
        estimation_trials.addData('mouse_estm.y', mouse_estm.y)
        estimation_trials.addData('mouse_estm.leftButton', mouse_estm.leftButton)
        estimation_trials.addData('mouse_estm.midButton', mouse_estm.midButton)
        estimation_trials.addData('mouse_estm.rightButton', mouse_estm.rightButton)
        estimation_trials.addData('mouse_estm.time', mouse_estm.time)
        # the Routine "main_estimation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'estimation_trials'
    
    
    # --- Prepare to start Routine "show_reward" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('show_reward.started', globalClock.getTime(format='float'))
    totalRewardText.setText('')
    # Run 'Begin Routine' code from code_5
    # Sum up all the values in the array
    #total_reward = sum(rewards_array)
    
    # Convert values to integers and then sum up
    #total_reward = sum([int(value) for value in rewards_array])
    
    # Convert values in rewards_array to integers
    rewards_array = [int(value) for value in rewards_array]
    
    total_reward = rewards_array[1]
    
    # Update the text component with the total reward
    totalRewardText.setText(f'Total Reward: {total_reward}')
    
    #totalRewardText.text = f'Total Reward: {total_reward}'
    
    #
    ## Update the text component with the total reward
    #totalRewardText.setText(f'Total Reward: {'5'}')
    #
    # keep track of which components have finished
    show_rewardComponents = [text4, totalRewardText]
    for thisComponent in show_rewardComponents:
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
    
    # --- Run Routine "show_reward" ---
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
        
        # *totalRewardText* updates
        
        # if totalRewardText is starting this frame...
        if totalRewardText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            totalRewardText.frameNStart = frameN  # exact frame index
            totalRewardText.tStart = t  # local t and not account for scr refresh
            totalRewardText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(totalRewardText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'totalRewardText.started')
            # update status
            totalRewardText.status = STARTED
            totalRewardText.setAutoDraw(True)
        
        # if totalRewardText is active this frame...
        if totalRewardText.status == STARTED:
            # update params
            pass
        
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
        for thisComponent in show_rewardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "show_reward" ---
    for thisComponent in show_rewardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('show_reward.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "show_reward" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    # Run 'End Experiment' code from training_code
    ## End Experiment
    ##
    ##win.close()
    ##core.quit()
    #
    #win.flip()
    #
    # Run 'End Experiment' code from learning_code
    ## End Experiment
    ##
    ##win.close()
    ##core.quit()
    #
    #win.flip()
    #
    # Run 'End Experiment' code from transfer_code
    ## End Experiment
    ##
    ##win.close()
    ##core.quit()
    #
    #win.flip()
    #
    # Run 'End Experiment' code from estimation_code
    ## End Experiment
    ##
    ##win.close()
    ##core.quit()
    #
    #win.flip()
    #
    
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
