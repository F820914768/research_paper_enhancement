import sqlite3


if __name__ == '__main__':
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()


    query = """
            SELECT i.ID, q.Institution_Name, q.Score
            FROM institution as i, QS as q
            WHERE i.Institution_Name = q.Institution_Name

    """

    cursor.execute(query)
    data = cursor.fetchall()
    print(len(data))