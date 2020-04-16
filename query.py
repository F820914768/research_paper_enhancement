# -*- coding: utf-8 -*-

import sqlite3
import pandas as pd

if __name__ == '__main__':
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()


    query = """
            SELECT i.ID, q.Institution_Name, q.Score, i.Institution_Name
            FROM institution as i LEFT JOIN QS as q ON q.Institution_Name = i.Institution_Name

    """

    cursor.execute(query)
    data = cursor.fetchall()
    

    df = pd.DataFrame(data)
    df.to_csv('institution_ranking.csv')
    print(df[2].isnull().sum())


        