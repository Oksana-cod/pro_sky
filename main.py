import json
import sqlite3
import flask

app = flask.Flask(__name__)


def get_value_from_db(sql):
    with sqlite3.connect("netflix.db") as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(sql).fetchall()

        return result


def search_by_title(title):
    sql = f'''
           select *
           from netflix
           where title = '{title}'
           order by release_year desc
           '''

    result = get_value_from_db(sql)
    for item in result:
        return dict(item)


@app.get("/movie/<title>")
def search_by_title_view(title):
    result = search_by_title(title=title)
    print(result)
    return app.response_class(
        response=json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json"
    )


@app.get("/movie/<year1>/to/<year2>")
def search_data_view(year1, year2):
    sql = f'''
        select title, release_year
        from netflix
        where release_year between '{year1}' and '{year2}'
    '''
    result = []
    for item in get_value_from_db(sql=sql):
        result.append(dict(item))
    return app.response_class(
        response=json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json"
        )


@app.get("/rating/<rating>/")
def search_rating_view(rating):
    my_dict = {
        "children": ("G", ""),
        "family": ("G", "PG", "PG-13"),
        "abult": ("R", "NC-17")
    }

    sql = f'''
        select title, rating, description
        from netflix
        where rating in {my_dict.get(rating, ("R", ""))}
        '''
    result = []

    for item in get_value_from_db(sql=sql):
        result.append(dict(item))

    return app.response_class(
        response=json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json"
    )


@app.get("/genre/<genre>/")
def search_genre_view(genre):
    sql = f'''
        select *
        from netflix
        where listed_in like '%{genre}'
        order by release_year desc
        limit 10
        '''

    result = []

    for item in get_value_from_db(sql=sql):
        result.append(dict(item))

    return app.response_class(
        response=json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json"
    )


def search_double_name(name1, name2):
    sql = f'''
    select "cast"
    from netflix
    where "cast" like  '%{name1}%' and "cast" like  '%{name2}%'
    '''
    result = []

    names_dict = {}
    for item in get_value_from_db(sql=sql):
        names = set(dict(item).get('cast').split(",")) - set([name1, name2])

        for name in names:
            names_dict[str(name).strip()] = names_dict.get(str(name).strip(), 0) + 1

    for key, value in names_dict.items():
        if value >= 2:
            result.append(key)

    return result


def step_6(typ, ear, genre):
    sql = f'''
    select title, description, listed_in
    from netflix
    where type = '{typ}'
    and release_year = '{ear}'
    and listed_in like '%{genre}%'
    '''

    result = []

    for item in get_value_from_db(sql):
        result.append(dict(item))
    return json.dumps(result, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    print(search_double_name('Rose McIver', 'Ben Lamb'))
    print(step_6('Movie', '2021', 'Documentaries'))

    #app.run(host='0.0.0.0',
          #  port=8080,
           # debug=True
          #  )
