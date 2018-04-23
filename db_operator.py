import sqlite3



pathToDb = 'task_list.db'


def start(bot, update):

    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    try:
        con = sqlite3.connect(pathToDb)
        # print("db correttamente aperto")
        # update.message.reply_text("your user id is: " + str(update.message.from_user.id))
        cur = con.cursor()
        cur.execute(
            "create table if not exists 'task' (id integer primary key autoincrement, user_id integer ,todo varchar[255] not null)")
        con.commit()
        cur.close()
        con.close()
    except sqlite3.DataError as DataErr:
        print("errore di creazione table " + DataErr.args[0])
    except sqlite3.DatabaseError as DBerror:
        print("errore nell'apertura del db " + DBerror.args[0])
        sys.exit(1)

def showTasks():
    try:
        con = sqlite3.connect(pathToDb)
        cur = con.cursor()
        # cur.execute("select todo from task order by todo where ?", (update.message.from_user.id,) )
        cur.execute("select todo from task order by todo")
        rows = cur.fetchall()
        cur.close()
    except sqlite3.DataError as DataErr:
        print("errore di creazione table " + DataErr.args[0])
    except sqlite3.DatabaseError as DBerror:
        print("errore nell'apertura del db " + DBerror.args[0])
        sys.exit(1)

    if len(rows) == 0:
        update.message.reply_text("no tasks memorized yet")
        return

    for line in rows:
        print(line[0])
        update.message.reply_text(line[0])



def newTask(arg):
    # msg = ' '.join(arg)
    if (arg != ""):

        con = sqlite3.connect(pathToDb)
        cur = con.cursor()
        cur.execute(
            "insert into task (todo) values (?)", (arg, ))
        con.commit()
        cur.close()
        con.close()

        # showTasks(bot, update)
        print("added " + msg + " to the tasks list")
    else:
        print("empty task...")


def removeTask(msg):
    # msg = ' '.join(args)
    try:
        con = sqlite3.connect(pathToDb)
        cur = con.cursor()
        cur.execute("delete from task where todo = ?", (msg, ))
        con.commit()
        cur.close()
        con.close()
        print(msg + " removed")
    except ValueError:
        print("element not found!")



def removeAllTasks(msg):
    con = sqlite3.connect(pathToDb)
    cur = con.cursor()
    cur.execute("delete from task where todo like ? ", (msg, ))
    con.commit()
    cur.close()
    con.close()
    print("Deleted ALL tasks containing " + msg)

# closeBot function not needed

def clean_db(bot, update):
    global pathToDb
    os.remove(pathToDb)
    with open(pathToDb, 'w'):
        os.utime(pathToDb, None)

