# Fake Shop (Only in Russian)
This project was created by me as a demonstration of the work of fake stores in Telegram. In the bot, you can configure all the buttons (for receiving responses), send a newsletter, change the settings and the name of the store.

Before setting up the store itself, you must specify the bot token and the administrator id. Developments in this area will no longer be carried out. This is the final version of the project.

After performing my research, the result showed that the creation of such stores is very simple in execution and does not carry any difficulties. Using my bot as an example, you can clearly see how fake stores, bots selling illegal substances, and many other projects in this area work.

> Attention! This project does not encourage the use of such programs. It was created for the purpose of obtaining information in the field of information security and as a clear example of the use of programming languages for bad purposes.

## Video on YouTube

[![Тут Название](https://img.youtube.com/vi/iOnkhi2pir0/0.jpg)](https://www.youtube.com/watch?v=iOnkhi2pir0)

## Required
* [Python 3.9.1](https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe) 
* [pyTelegramBotApi 3.7.4](https://pypi.org/project/pyTelegramBotAPI/)
* [SimpleQIWI](https://github.com/Emberium/SimpleQIWI)

## How to use
* Install the script
* Edit `token` and `admin_id` in config.py
* [Download Telegram](https://desktop.telegram.org/)
* Launch the bot!

# Instruction

#### First Step
1) First, you need to install [Telegram](https://desktop.telegram.org/) on your PC and register in the messenger. Find in search `@BotFather` – this is the father of all bots in telegram, it is he who creates them.
2) You write `/newbot` and answer two simple questions: the name of the bot and its username. After that, @BotFather will congratulate us on the successful creation of the bot and send us its token (save it).

 
> Attention! The token is the only identification key to the bot. Do not post it anywhere, otherwise other people will be able to control your bot.


3) Go to telegram and search in the search - `@getidsbot`. Click `/start`, after that the bot will send us a large message with detailed information about our account. Of all this, we only need the id (save it).
4) Download any code editor (for example, VisualStudio Code, sublime text or atom). Install it. Now we will need to change a couple of file values config.py. We go to ScamShopv2.0.rar --> ScamShopv2. 0 --> bot --> config.py (open it through the code editor)
5) Find the column `token` and `admin_id` and change them to our values. Save it.
                               

#### Launching the bot via the console

1) Creating a separate folder for the bot. We transfer the files from the archive there.
2) Go to cmd.
3) Typing

```
cd C:\your folder path
```
```
pip install virtualenv
```
```
python -m venv venv
```
```
venv\Scripts\actiavte
```
```
pip install -r requirements.txt
```
The bot is running!

#### Launching a bot on a remote server ####

You don't want to leave your own PC running 24/7, and it's not practical. We buy VDS (Virtual Dedicated Server, virtual dedicated server) - a remote PC on which a certain amount of power and memory is allocated for you, and to the command line of which you are given access. Most often, the operating system of such a machine will be linux. The fee is small-10$/month, so without much moral suffering, I paid for a VDS based on Debian GNU / Linux and began to figure out how to enable the bot on a remote server.
How do you connect to VDS?

There are different methods, but you will install it over an SSH connection via Putty. Download Putty via the official website and open it. Enter the IP-address of the VDS and click open. A window should open where you need to enter your username and password from the server. All the above-mentioned data will be issued by the company from which you will purchase the VDS. Next, the VDS server.

How do you install all the programming languages and libraries you need on the server?

Here everything is simple. By entering these 5 commands into the server console in this sequence, you will install python3, setuptools, pip3, and the pyTelegramBotAPI library on the server.


```
apt-get update
```
```
apt-get install python3
```
```
apt-get install python3-setuptools
```
```
apt-get install python3-pip
```
```
pip3 install pyTelegramBotAPI
```

All additional libraries that are not included in the main package of python3 must also be installed on the principle.

```
pip3 install ‘name_of_site_package’
```


How do I upload files from my PC to the server?

First, we will create a folder in which we will fill all the necessary files. On the server, go to the /usr/local/bin directory and create the bot folder.

```
cd /usr/local/bin
```
```
mkdir bot
```

I have windows installed on my PC, respectively, and the commands will be for the windows command line. First, you need to go to the directory where it is located putty.exe.

```
cd /program files/putty
```

Next, download bot.py, which is located in the catalog C:\Users\Ilya\PycharmProjects\Bot (you need to substitute your directory) in the directory on the server /usr/local/bin/bot.

```
pscp.exe "C:\Users\admin\Bot\app.py" root@123.123.12.12:/usr/local/bin/bot
```

Line root@123.123.12.12 you need to replace it with a line like login@IP_address, respectively, with your username and IP address (mentioned above in the section " How do I connect to VDS?"). Replacing bot.py on the names of other files, download all the necessary ones.


How do I download files from a server to a PC?

The same as when uploading files to the server on the command line to the directory where it is located putty.exe. And enter this command to download the database file to the desktop of your PC.

```
pscp.exe root@123.123.12.12:/usr/local/bin/bot/database "C:\Users\admin\Desktop
```


How do I launch a bot?

The first and easiest option is to go to the directory with the executable files and register python3 bot.py, but then when you close putty, the bot will shut down.

The second option is to launch the bot using the screen module, which creates parallel desktops, but then the bot will not restart automatically in the event of a crash, and this happens often-several times a week due to the nightly restart of telegram servers (at 3: 00 Moscow Time).

The third method is systemd-system manager, a daemon for initializing other daemons in Linux. Simply put, systemd will launch the bot and will restart it if it crashes.

Install systemd:

```
apt-get install systemd
```

Create a file on your PC named bot. service with the following content:


###### Unit
```
Description=Fake Shop (Telegram Bot)
After=syslog.target
After=network.target
```

###### Service
```
Type=simple
User=root
WorkingDirectory=/usr/local/bin/bot
ExecStart=/usr/bin/python3 /usr/local/bin/bot/app.py
RestartSec=10
Restart=always
```

###### Install
```
WantedBy=multi-user.target
```

And upload it to the desired folder:

```
pscp.exe "C:\Users\Ilya\PycharmProjects\Bot\bot.service" root@123.123.12.12:/etc/systemd/system
```

Next, you need to register 4 commands in the server console:

```
systemctl daemon-reload
```
```
systemctl enable bot
```
```
systemctl start bot
```
```
systemctl status bot
```

In my case, due to certain implementation errors, specifically multithreading, I had to transfer the function to calculate the battles (battle_counter.py) in a separate daemon.


###### Unit
```
Description=Fake Shop (Telegram Bot)
After=syslog.target
After=network.target
```

######  Service
```
Type=simple
User=root
WorkingDirectory=/usr/local/bin/bot
ExecStart=/usr/bin/python3 /usr/local/bin/bot/app.py
RestartSec=10
Restart=always
```

###### Install
```
WantedBy=multi-user.target
```

After that, you should see a message with something like this content:



Your bot is up and running!
