import psycopg2
import psycopg2.extras
from domain.producto.productomodel import ProductoModel

class ProductoInfrastructure:

    ##############################################################
    def IngresarProducto(self, productomodel: ProductoModel):
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
                cur.execute(
                    "SELECT spaIngresarProducto(%s, %s, %s, %s, %s, %s, %s);",
                    (
                        productomodel.Nombre,
                        productomodel.Descripcion,
                        productomodel.Precio,
                        productomodel.Stock,
                        productomodel.IdCategoria,
                        productomodel.IdMarca,
                        productomodel.IdModelo
                    )
                )
                result = cur.fetchone()[0]
                conn.commit()
                return result

        except Exception as e:
            print("Error al ingresar producto:", e)
            return None

        finally:
            if conn:
                conn.close()

    ##############################################################
    def ConsultarProducto(self):
        conn = None
        try:
            conn = psycopg2.connect(
                dbname="dbtiendaelectro",
                user="postgres",
                password="",
                host="127.0.0.1",
                port="5432"
            )

            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT spaConsultarProducto();")
                result = cur.fetchall()
                return result

        except Exception as e:
            print("Error al consultar producto:", e)
            return []

        finally:
            if conn:
                conn.close()
