# RWDL

**RWDL** is deep learning algoritm that hide watermarks on image.

This is my DNN project. This project is focused on removing watermarks from photos. The purpose of this project is to simply remove watermarks from photos using a [Telegram bot](http://t.me/RWDLBOT)

## What is this project based on?

This projet used autoencoder. All information about model, you can see in notebook.

## How to use this project?

If you want to run a telegram bot, you need to create one in [BotFather](@BotFather). Then you need to create file "constants.py" and in it write

```py
TOKEN = "YOUR TOKEN"
```

After that you can build the docker image.

If you want to check if the network works, you have to install the packages from requirements.txt

``` py
pip install -r requirements.txt
```

Next run the loadImage file (you can put your picture in mnt/img). You can run loadImage like this:

```py
python src/loadImge.py
```

### Database used in this project

[Watermarks Dataset](https://www.kaggle.com/therealcyberlord/watermark-removal-using-convolutional-autoencoder/data)

## These are the results of the autoencoder work

![Results](/mnt/results/results.png "Results")
