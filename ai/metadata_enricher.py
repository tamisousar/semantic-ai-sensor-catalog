# ai/metadata_enricher.py

import re
import spacy

# Carrega modelo leve de linguagem (em inglês)
# Se for rodar localmente, execute antes: python -m spacy download en_core_web_sm
try:
    nlp = spacy.load("en_core_web_sm")
except:
    nlp = None

class MetadataEnricher:
    """
    AI-based metadata enrichment for sensors from PI System or other SCADA sources.
    """

    def __init__(self):
        self.keywords = {
            "pressure": {"type": "PressureSensor", "unit": "Pa"},
            "temperature": {"type": "TemperatureSensor", "unit": "°C"},
            "current": {"type": "CurrentSensor", "unit": "A"},
            "speed": {"type": "RotationalSpeedSensor", "unit": "rpm"},
            "level": {"type": "LevelSensor", "unit": "%"},
            "vacuum": {"type": "VacuumSensor", "unit": "kPa"},
        }

    def enrich(self, sensor):
        """
        Recebe metadados brutos e adiciona informações inferidas por IA.
        """
        description = sensor.get("description", "").lower()
        name = sensor.get("name", "").lower()
        text = f"{name} {description}"

        enriched = sensor.copy()

        # 🔹 Identificação por palavras-chave
        for key, data in self.keywords.items():
            if key in text:
                enriched["ai_detected_type"] = data["type"]
                enriched["ai_suggested_unit"] = data["unit"]

        # 🔹 Sugestão de fabricante (exemplo simples com NLP)
        if nlp:
            doc = nlp(text)
            orgs = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
            if orgs:
                enriched["ai_detected_manufacturer"] = orgs[0]

        # 🔹 Classificação por padrão de nome
        if re.search(r"motor|pump|compressor", text):
            enriched["ai_suggested_category"] = "Rotating Equipment"
        elif re.search(r"boiler|heater", text):
            enriched["ai_suggested_category"] = "Thermal Equipment"
        elif re.search(r"tank|vessel", text):
            enriched["ai_suggested_category"] = "Storage Equipment"

        return enriched


# Exemplo de uso isolado:
if __name__ == "__main__":
    enricher = MetadataEnricher()
    example_sensor = {
        "name": "PUMP101_PRESS",
        "description": "Vacuum pressure sensor for pump 101",
    }
    enriched = enricher.enrich(example_sensor)
    print(enriched)

