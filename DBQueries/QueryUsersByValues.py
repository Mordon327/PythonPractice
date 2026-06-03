app = Flask(__name__)

DATABASE = os.path.join(app.root_path, 'databases/pythonPracticeDB')
class UsersTable:
    """docstring for UsersTable"""
    def __init__(self, arg):
        super(UsersTable, self).__init__()
        self.arg = arg

    def connect_db():
        app = Flask(__name__)
        sql = sqlite3.connect(os.path.join(app.root_path, 'databases/pythonPracticeDB'))
        sql.row_factory = sqlite3.Row
    return sql

    def get_db(g):
        if not hasattr(g, 'sqlite3'):
            g.sqlite_db = connect_db()
        return g.sqlite_db

    def getUsers():
        db = get_db()
    cursor = db.execute('SELECT * FROM users WHERE ID = ?', [user_id])
    result = cursor.fetchone()

        

# 1. Connect to the database (creates 'example.db' if it doesn't exist)
    conn = get_dbs()

# 2. Create a cursor object to interact with the database
    cursor = conn.cursor()

# 3. Execute a query
    cursor.execute("SELECT * FROM Users")

# 4. Fetch all results as a list of tuples
    rows = cursor.fetchall()
    conn.close()
    return rows