import os
from requests import *
from dotenv import load_dotenv

load_dotenv()

url = os.environ.get("HASS_URL")
token = os.environ.get("HASS_TOKEN")
headers = {
    "Authorization": "Bearer {token}".format(token=token),
    "Content-Type": "application/json",
}

def get_states(entity_ids = []):
  resJson = []
  try:
    res = get(
      "{host}/api/states".format(host=url), 
      headers=headers,
      timeout=5
    )
    resJson = res.json()
  except exceptions.RequestException as e:
    print(e, flush=True)
  states = {}
  for entity_id in entity_ids:
    states[entity_id] = ""
    for new_state in resJson:
      # to infer based on individual light entity ids such as "hallway_fridge"
      # groups of ikea lights don't show up in the states as areas, but are still switchable.
      if entity_id in new_state["entity_id"]:
        states[entity_id] = new_state["state"]
        break
  return states

def switch_area(area_id, state):
  print(
    "Switching area {area_id} to {state}".format(area_id=area_id, state=state),
    flush=True
  )
  try:
    res = post(
      "{host}/api/services/light/turn_{state}".format(host=url, state=state), 
      headers=headers, 
      timeout=5,
      json={"area_id": area_id}
    )
  except exceptions.RequestException as e:
    print(e, flush=True)
