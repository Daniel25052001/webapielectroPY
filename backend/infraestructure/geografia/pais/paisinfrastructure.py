import psycopg2
import psycopg2.extras
from domain.geografia.pais import PaisModel
class PaisInfrastructure:

    def __init__(self):
        pass







    ##############################################################
def IngresarPais(self, paismodel: PaisModel):
        conn = None
        try:
            conn = psycopg2.connect(
                dbname="dbtiendaelectro",
                user="postgres",
                password="",
                host="127.0.0.1",
                port="5432"
            )

            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarPais(%s);", (paismodel.Nombre,))
                result = cur.fetchone()[0]
                conn.commit()
                result = 1
            return result 

        except Exception as e:
            print("Error al ingresar país:", e)
            return None

        finally:
            if conn:
                conn.close()


  















    ##############################################################
def ConsultarPais(self):
        try:
            conn = psycopg2.connect(
                dbname="dbtiendaelectro",
                user="postgres",
                password="",
                host="127.0.0.1",
                port="5432"
            )

            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT spaConsultarPais();")
                result = cur.fetchall()
                return result

        except Exception as e:
            print("Error al consultar país:", e)
            return []

        finally:
            if conn:
                conn.close()
   
                                
        

         