# LaTeX Speech Recognition

## General Information

* Language: Python
  * Modules:
    * SpeechRecognition
    * (Possibly) PyAudio
* Article we're reading to begin learning for this project: [Python Speech Recognition](https://realpython.com/python-speech-recognition/)

## Beginning (Pick a better name later)

### The `Recognizer` Class

* We import SpeechRecognition like so: `import speech_recognition as sr`
* The `Recognizer` class in general
  * All the magic of SpeechRecognition happens in the `Recognizer` class
  * It's meant to recognize the speech ==(this is obvious and probably an unnecessary point)==
  * Each `Recognizer` instance comes with settings and functionality for recognizing speech from an audio source
  * Initialize like so: `r = sr.Recognizer()`
  * `Recognizer` comes with seven methods for recognizing speech. The article we're reading uses the [Google Web Speech API](https://wicg.github.io/speech-api/), so we're going to be referring to that in this document.

### Google Web Speech

* As mentioned before, we'll be using the Google Web Speech API to begin this project. We begin by calling `r.recognize_google()`, which calls the Web Speech API. From this, we get an error that says we're missing an argument `audio_data`. `audio_data` is the audio file the function is supposed to interpret speech from.

### Audio Files

* `audio_data` must be an instance of SpeechRecognition's `AudioData` class. There are two ways to create an `AudioData` instance: from an audio file or audio from the microphone. We'll be working with pre-recorded audio files for now.

* To work with audio files, we'll need to utilize SpeechRecognition's `AudioFile` class. This way, we can pass it a path to an audio file and begin working with the file.

* SpeechRecognition recognizes the following file formats:

  * WAV
  * AIFF
  * AIFF-C
  * Native FLAC

* To initialize an audio file, call `file = sr.AudioFile(path)`.  We use `audio = r.record(src)` to process the audio file. `src` is `file`. 

* Now we can run `r.recognize_google(audio)` to get an interpretation of the audio file `audio`.

  Here's what we'll currently have written in Python to make this work:

  ```python
  file = sr.AudioFile(/path/to/file)
  with file as src:
  	audio = r.record(src)
  r.recognize_google(audio)
  ```
  * Note: `with expression as variable`  is a with block. It's a control flow structure that clarifies code that would use a `try...finally` block.

* Now that we're able to transcribe speech, we can now look at other features. With `record()`, we can capture segments of audio with an offset and a set duration of the audio file. `record()` has two optional parameters: `offset` and `duration`.

  For example, if we only wanted to transcribe the first 10 seconds of an audio file, we would call:

  ````python
  with file as src:
    audio = r.record(src, duration=10)
  ````

  