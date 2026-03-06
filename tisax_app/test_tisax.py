"""
TISAX Assessment Logic Tests
Tests all combinations and edge cases
"""

from tisax_logic import TISAXAssessment


def test_case(name, data, expected_tisax, expected_al, expected_labels):
    """Test a single assessment case"""
    assessment = TISAXAssessment()
    assessment.set_data(**data)
    result = assessment.assess()
    
    tisax_match = result['tisax_required'] == expected_tisax
    al_match = result['assessment_level'] == expected_al if expected_tisax else True
    labels_match = set(result['labels']) == set(expected_labels)
    
    status = "✅" if (tisax_match and al_match and labels_match) else "❌"
    
    print(f"\n{status} {name}")
    print(f"   TISAX Required: {result['tisax_required']} (expected: {expected_tisax})")
    if expected_tisax:
        print(f"   Level: {result['assessment_level']} (expected: {expected_al})")
        print(f"   Labels: {sorted(result['labels'])}")
        print(f"   Expected: {sorted(expected_labels)}")
    
    return tisax_match and al_match and labels_match


def run_tests():
    """Run comprehensive test suite"""
    print("=" * 60)
    print("TISAX Assessment Logic Test Suite")
    print("=" * 60)
    
    all_passed = True
    
    # TEST 1: NO TISAX - Missing k1 (all infosec off)
    all_passed &= test_case(
        "TEST 1: No TISAX - Missing Infosec (k1)",
        {
            "vertraulichkeit": "Öffentlich",
            "integritat": "Kein",
            "verfugbarkeit": "Kein",
            "personenbezogene_daten": True,
            "besondere_kategorien": False,
            "bauteile": True
        },
        expected_tisax=False,
        expected_al=None,
        expected_labels=[]
    )
    
    # TEST 2: NO TISAX - Missing k2 (no datenschutz)
    all_passed &= test_case(
        "TEST 2: No TISAX - Missing Datenschutz (k2)",
        {
            "vertraulichkeit": "Intern",
            "integritat": "Normaler",
            "verfugbarkeit": "Normaler",
            "personenbezogene_daten": False,
            "besondere_kategorien": False,
            "bauteile": True
        },
        expected_tisax=False,
        expected_al=None,
        expected_labels=[]
    )
    
    # TEST 3: NO TISAX - Missing k3 (no prototypenschutz)
    all_passed &= test_case(
        "TEST 3: No TISAX - Missing Prototypenschutz (k3)",
        {
            "vertraulichkeit": "Intern",
            "integritat": "Normaler",
            "verfugbarkeit": "Normaler",
            "personenbezogene_daten": True,
            "besondere_kategorien": False,
            "bauteile": False,
            "fahrzeuge": False,
            "erprobung": False,
            "events": False
        },
        expected_tisax=False,
        expected_al=None,
        expected_labels=[]
    )
    
    # TEST 4: YES TISAX - AL1 (all minimum)
    all_passed &= test_case(
        "TEST 4: YES TISAX - AL1 (Normal)",
        {
            "unternehmensname": "Test Corp",
            "vertraulichkeit": "Intern",
            "integritat": "Normaler",
            "verfugbarkeit": "Normaler",
            "personenbezogene_daten": True,
            "besondere_kategorien": False,
            "bauteile": True
        },
        expected_tisax=True,
        expected_al="AL1",
        expected_labels=["Data", "Proto Parts", "confidential"]
    )
    
    # TEST 5: YES TISAX - AL2 (High integrity)
    all_passed &= test_case(
        "TEST 5: YES TISAX - AL2 (High)",
        {
            "vertraulichkeit": "Intern",
            "integritat": "Hoher",
            "verfugbarkeit": "Normaler",
            "personenbezogene_daten": True,
            "besondere_kategorien": False,
            "bauteile": False,
            "fahrzeuge": True,
            "erprobung": False,
            "events": False
        },
        expected_tisax=True,
        expected_al="AL2",
        expected_labels=["Data", "Proto Vehicles", "confidential", "high availability"]
    )
    
    # TEST 6: YES TISAX - AL3 (Secret + Very High)
    all_passed &= test_case(
        "TEST 6: YES TISAX - AL3 (Very High)",
        {
            "vertraulichkeit": "Geheim - Sehr hoher",
            "integritat": "Normaler",
            "verfugbarkeit": "Normaler",
            "personenbezogene_daten": True,
            "besondere_kategorien": False,
            "bauteile": False,
            "fahrzeuge": False,
            "erprobung": True,
            "events": False
        },
        expected_tisax=True,
        expected_al="AL3",
        expected_labels=["Data", "Test Vehicles", "confidential", "strictly confidential", "very high availability"]
    )
    
    # TEST 7: YES TISAX - AL3 (Very high availability)
    all_passed &= test_case(
        "TEST 7: YES TISAX - AL3 (Very High Availability)",
        {
            "vertraulichkeit": "Intern",
            "integritat": "Normaler",
            "verfugbarkeit": "Sehr hoher",
            "personenbezogene_daten": False,
            "besondere_kategorien": True,
            "bauteile": False,
            "fahrzeuge": False,
            "erprobung": False,
            "events": True
        },
        expected_tisax=True,
        expected_al="AL3",
        expected_labels=["Events + Shootings", "Special Data", "confidential", "strictly confidential", "very high availability"]
    )
    
    # TEST 8: YES TISAX - Multiple prototypes
    all_passed &= test_case(
        "TEST 8: YES TISAX - Multiple Prototypes",
        {
            "vertraulichkeit": "Vertraulich - Hoher",
            "integritat": "Hoher",
            "verfugbarkeit": "Normaler",
            "personenbezogene_daten": True,
            "besondere_kategorien": True,
            "bauteile": True,
            "fahrzeuge": True,
            "erprobung": True,
            "events": True
        },
        expected_tisax=True,
        expected_al="AL2",
        expected_labels=[
            "confidential", "high availability", "Data", "Special Data",
            "Proto Parts", "Proto Vehicles", "Test Vehicles", "Events + Shootings",
            "strictly confidential"
        ]
    )
    
    # TEST 9: YES TISAX - Only besondere_kategorien
    all_passed &= test_case(
        "TEST 9: YES TISAX - Only Special Data Category",
        {
            "vertraulichkeit": "Intern",
            "integritat": "Normaler",
            "verfugbarkeit": "Normaler",
            "personenbezogene_daten": False,
            "besondere_kategorien": True,
            "bauteile": True
        },
        expected_tisax=True,
        expected_al="AL1",
        expected_labels=["Proto Parts", "Special Data", "confidential", "strictly confidential"]
    )
    
    # TEST 10: Edge case - All questions NO/Kein
    all_passed &= test_case(
        "TEST 10: All Questions No/None",
        {
            "vertraulichkeit": "Öffentlich",
            "integritat": "Kein",
            "verfugbarkeit": "Kein",
            "personenbezogene_daten": False,
            "besondere_kategorien": False,
            "bauteile": False,
            "fahrzeuge": False,
            "erprobung": False,
            "events": False
        },
        expected_tisax=False,
        expected_al=None,
        expected_labels=[]
    )
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✅ ALL TESTS PASSED!")
    else:
        print("❌ SOME TESTS FAILED")
    print("=" * 60)
    
    return all_passed


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
