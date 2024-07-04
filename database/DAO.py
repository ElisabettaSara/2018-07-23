from database.DB_connect import DBConnect
from model.state import State


class DAO():


    @staticmethod
    def getAnno():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct year(`datetime`) as anno
                    from sighting s """

        cursor.execute(query,)
        for row in cursor:
            result.append(row['anno'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from state s """

        cursor.execute(query, )
        for row in cursor:
            result.append(State(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(anno, giorni):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select n.state1 as stato1, n.state2 as stato2, count(*) as peso
                    from neighbor n , sighting s1, sighting s2  
                    where n.state1 =s1.state  and n.state2 =s2.state 
                          and year(s1.`datetime` )=%s and year(s2.`datetime` )=%s
                          and abs(datediff(s1.`datetime`, s2.`datetime`))<=%s 
                          and s1.state<s2.state
                    group by n.state1 , n.state2  """

        cursor.execute(query, (anno, anno, giorni,) )
        for row in cursor:
            result.append((row['stato1'], row['stato2'], row['peso']))

        cursor.close()
        conn.close()
        return result

