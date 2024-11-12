from fastapi import FastAPI

app = FastAPI()

@app.get("/reservations")
def get_reservations():
    return {"message": "Voilà les réservations"}

@app.get("/reservations/{reservation_id}")
def get_reservation(reservation_id: int):
    return {"message": f"Voilà la réservation {reservation_id}"}

@app.post("/reservations")
def create_reservation():
    return {"message": "La réservation a été créée avec succès"}

@app.put("/reservations/{reservation_id}")
def update_reservation(reservation_id: int):
    return {"message": f"La réservation {reservation_id} a été modifiée avec succès"}

@app.delete("/reservations/{reservation_id}")
def delete_reservation(reservation_id: int):
    return {"message": f"La réservation {reservation_id} a été supprimée avec succès"}