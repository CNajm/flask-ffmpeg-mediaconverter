# Flask-FFmpeg Media Converter

## About

This is a WIP project that interfaces an audio converter powered by ffmpeg using flask, and my self-driven project for ICT 12 - October/November 2017.  

This was my first dive into flask and standalone back-ends. I will be adding and improving to this in the future, but this is what I have so far.

## Built With

* [Flask](http://flask.pocoo.org)
* [ffmpeg](https://www.ffmpeg.org)

## Deploying

Download and extract, you will also need whatever FFmpeg binary runs on your system linked to using the FFMPEG_BIN variable. Run it like any flask app.

1. With flask installed (`pip install flask`),  
2. Set the environment variable with `set FLASK_APP=main01.py` for windows or `export FLASK_APP=main01.py` for linux,  
3. Use `flask run`,  
4. Navigate to `localhost:5000` in your browser.  
