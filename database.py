from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://avnadmin: AVNS_pw9PoJOC1YqTZpD6nsX@apex-real-estate-apex-real-estate.a.aivencloud.com/defaultdb?charset=utf8mb4")

with engine.connect as conn:
  result = conn.execute(text("select * from listings"))
  print(result.all())