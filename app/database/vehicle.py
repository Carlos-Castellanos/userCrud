#   id integer primary key autoincrement,
#   id_user integer,
#   style text not null,
#   color text not null,
#   wheels integer not null,


from app.database import get_db

def output_formatter(results):
    out = []
    for result in results:
        vehicle = {
            "id": result[0],
            "id_user": result[1],
            "style":result[2],
            "color":result[3],
            "wheels": result[4]
        }
        out.append(vehicle)
    return out

def scan():
    cursor =get_db().execute(
        "SELECT * FROM vehicles",()
    )
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def select_by_id(pk):
    cursor =get_db().execute(
        "SELECT * FROM vehicles WHERE id=?",
        (pk,)
    )
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def insert(vehicle_dict):      
    value_tuple = (
        vehicle_dict.get("id_user"),
        vehicle_dict.get("style"),
        vehicle_dict.get("color"),
        vehicle_dict.get("wheels")
    )
    statement = """
        INSERT INTO vehicles (
            id_user,
            style,
            color,
            wheels
        ) VALUES (?,?,?,?)
    """
    cursor =get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()


def update(pk, vehicle_data):
    value_tuple = (
        vehicle_data.get("id_user"),
        vehicle_data.get("style"),
        vehicle_data.get("color"),
        vehicle_data.get("wheels"),
        pk
    )
    statement = """
        UPDATE  vehicles SET
        id_user=?,
        style=?,
        color=?,
        wheels=?
        WHERE id=?
    """
    cursor =get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()




# def deactivate(pk):
#     cursor =get_db()
#     cursor.execute("UPDATE vehicles SET wheels=0 WHERE id=?", (pk,))
#     cursor.commit()
#     cursor.close()






