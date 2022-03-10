import MySQLdb

conn = MySQLdb.connect(db='scraping', user='scraper', passwd='password', charset='utf8mb4')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS cities')
c.execute()
conn.commit()
conn.close()