"""
TISAX Risk Assessment Logic Module
Implements the matching logic for TISAX requirement determination
Based on extracted JavaScript from official Porsche TISAX PDF
"""

class TISAXAssessment:
    """
    Core TISAX assessment logic handler
    
    Rules:
    - k1 (Infosec): ALL three must be selected (≠ "Off")
    - k2 (Datenschutz): BOTH must be selected (≠ "Off")
    - k3 (Prototypenschutz): ALL four must be selected (≠ "Off")
    
    Result only calculated if ALL (k1 AND k2 AND k3) are true
    """
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Reset assessment data"""
        self.data = {
            "unternehmensname": "",
            "abteilung": "",
            "kontaktperson": "",
            "datum": None,
            "vertraulichkeit": "Off",
            "integritat": "Off",
            "verfugbarkeit": "Off",
            "personenbezogene_daten": "Off",
            "besondere_kategorien": "Off",
            "bauteile": "Off",
            "fahrzeuge": "Off",
            "erprobung": "Off",
            "events": "Off"
        }
    
    def check_k1_infosec(self) -> bool:
        """
        Check Information Security requirement (k1)
        ALL three must be selected (≠ "Off")
        """
        return (self.data["vertraulichkeit"] != "Off" and 
                self.data["integritat"] != "Off" and 
                self.data["verfugbarkeit"] != "Off")
    
    def check_k2_datenschutz(self) -> bool:
        """
        Check Data Protection requirement (k2)
        BOTH must be selected (≠ "Off")
        """
        return (self.data["personenbezogene_daten"] != "Off" and 
                self.data["besondere_kategorien"] != "Off")
    
    def check_k3_prototypenschutz(self) -> bool:
        """
        Check Prototype Protection requirement (k3)
        ALL four must be selected (≠ "Off")
        """
        return (self.data["bauteile"] != "Off" and 
                self.data["fahrzeuge"] != "Off" and 
                self.data["erprobung"] != "Off" and 
                self.data["events"] != "Off")
    
    def determine_protection_level(self) -> str:
        """
        Determine protection level (AL3, AL2, or AL1)
        Based on Information Security selections
        """
        # AL3: Sehr hoher Schutzbedarf
        if (self.data["vertraulichkeit"] == "Geheim - Sehr hoher Schutzbedarf" or
            self.data["integritat"] == "Sehr hoher Schutzbedarf" or
            self.data["verfugbarkeit"] == "Sehr hoher Schutzbedarf"):
            return "AL3"
        
        # AL2: Hoher Schutzbedarf
        if (self.data["vertraulichkeit"] == "Vertraulich - Hoher Schutzbedarf" or
            self.data["integritat"] == "Hoher Schutzbedarf" or
            self.data["verfugbarkeit"] == "Hoher Schutzbedarf"):
            return "AL2"
        
        # AL1: Normal / Kein Schutzbedarf
        return "AL1"
    
    def get_protection_description(self, level: str) -> str:
        """Get protection level description"""
        if level == "AL3":
            return "Schutzbedarf: sehr hoch"
        elif level == "AL2":
            return "Schutzbedarf: hoch"
        else:
            return "Schutzbedarf: normal"
    
    def assess(self) -> dict:
        """
        Run complete TISAX assessment
        Returns result dictionary
        """
        # Check all requirements
        k1 = self.check_k1_infosec()
        k2 = self.check_k2_datenschutz()
        k3 = self.check_k3_prototypenschutz()
        
        # Form is only valid if ALL sections are filled
        form_complete = k1 and k2 and k3
        
        result = {
            "form_complete": form_complete,
            "k1_infosec": k1,
            "k2_datenschutz": k2,
            "k3_prototypenschutz": k3,
            "tisax_required": None,
            "assessment_level": None,
            "result_text": "",
            "data": self.data.copy()
        }
        
        # Only assess if form is complete
        if not form_complete:
            result["tisax_required"] = None
            result["result_text"] = ""
            return result
        
        # Determine protection level
        level = self.determine_protection_level()
        result["assessment_level"] = level
        
        # Decision logic:
        # - AL3 or AL2: TISAX required
        # - AL1: Check if ANY Datenschutz/Prototyp = "Ja"
        
        if level in ["AL3", "AL2"]:
            result["tisax_required"] = True
            result["result_text"] = (
                "Ein aktuelles, gültiges TISAX-Zertifikat im ENX-Portal, "
                "mit einem Umfang, der die für dieses Projekt relevanten "
                "Standorte, Dienstleistungen und Prozesse abdeckt, mindestens "
                "gemäß den oben genannten TISAX-Labels.\n\n"
                "Der Nachweis des TISAX-Ergebnisses ist eine Voraussetzung "
                "für die Teilnahme Ihres Unternehmens an der Ausschreibung "
                "und für die Berücksichtigung bei einem anschließenden Vertragsabschluss.\n\n"
                "Ohne den rechtzeitigen und vollständigen Nachweis eines gültigen "
                "TISAX-Ergebnisses ist eine Teilnahme an der Ausschreibung der "
                "Porsche AG für diesen Projektumfang nicht möglich.\n\n"
                "Bitte senden Sie uns Ihren TISAX-Nachweis (z.B. über die Freigabe "
                "im ENX-Portal unter folgender Participant ID PPW911 und zusätzlich "
                "über die Assessment ID) an Ihre bekannte Kontaktadresse und bestätigen Sie."
            )
        else:
            # AL1: Check if any Datenschutz or Prototyp = "Ja"
            any_datenschutz_ja = (self.data["personenbezogene_daten"] == "Ja" or
                                  self.data["besondere_kategorien"] == "Ja")
            any_prototyp_ja = (self.data["bauteile"] == "Ja" or
                               self.data["fahrzeuge"] == "Ja" or
                               self.data["erprobung"] == "Ja" or
                               self.data["events"] == "Ja")
            
            if any_datenschutz_ja or any_prototyp_ja:
                result["tisax_required"] = True
                result["result_text"] = (
                    "Ein aktuelles, gültiges TISAX-Zertifikat im ENX-Portal, "
                    "mit einem Umfang, der die für dieses Projekt relevanten "
                    "Standorte, Dienstleistungen und Prozesse abdeckt, mindestens "
                    "gemäß den oben genannten TISAX-Labels.\n\n"
                    "Der Nachweis des TISAX-Ergebnisses ist eine Voraussetzung "
                    "für die Teilnahme Ihres Unternehmens an der Ausschreibung "
                    "und für die Berücksichtigung bei einem anschließenden Vertragsabschluss.\n\n"
                    "Ohne den rechtzeitigen und vollständigen Nachweis eines gültigen "
                    "TISAX-Ergebnisses ist eine Teilnahme an der Ausschreibung der "
                    "Porsche AG für diesen Projektumfang nicht möglich.\n\n"
                    "Bitte senden Sie uns Ihren TISAX-Nachweis (z.B. über die Freigabe "
                    "im ENX-Portal unter folgender Participant ID PPW911 und zusätzlich "
                    "über die Assessment ID) an Ihre bekannte Kontaktadresse und bestätigen Sie."
                )
            else:
                result["tisax_required"] = False
                result["result_text"] = "Kein TISAX-Zertifikat notwendig."
        
        return result
    
    def set_data(self, **kwargs):
        """Update assessment data"""
        for key, value in kwargs.items():
            if key in self.data:
                self.data[key] = value
