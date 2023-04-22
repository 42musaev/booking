from fastapi import FastAPI

app = FastAPI()


@app.get('/hotels')
def get_hotels():
    return [
        {
            'name': 'Moscow hotel',
            'price': '$4500',
        },
        {
            'name': 'St.Petersburg hotel',
            'price': '$4500',
        }
    ]
