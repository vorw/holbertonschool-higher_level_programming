import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for i, person in enumerate(attendees, start=1):
        safe_values = {}
        for key in placeholders:
            raw_value = person.get(key)
            if raw_value is None or raw_value == "":
                safe_values[key] = "N/A"
            else:
                safe_values[key] = str(raw_value)

        filled = template
        for key in placeholders:
            filled = filled.replace("{" + key + "}", safe_values[key])

        index = i
        filename = f"output_{index}.txt"
        while os.path.exists(filename):
            index += 1
            filename = f"output_{index}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(filled)

        print(f"Created: {filename}")
