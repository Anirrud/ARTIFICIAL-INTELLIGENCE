% Facts about symptoms and diseases
symptom(fever, [flu, cold, malaria]).
symptom(cough, [flu, cold]).
symptom(headache, [flu, migraine]).
symptom(rash, [allergy, measles]).
symptom(runny_nose, [flu, cold]).
symptom(fatigue, [flu, malaria]).
symptom(sneezing, [cold, allergy]).
symptom(chills, [malaria, flu]).

% Rule to diagnose a disease based on symptoms
diagnose(Disease, Symptoms) :-
    symptom(Symptom, Diseases),
    member(Symptom, Symptoms),
    member(Disease, Diseases).

% Predicate to find possible diseases based on symptoms
possible_diseases(Symptoms, Diseases) :-
    findall(Disease, diagnose(Disease, Symptoms), Diseases).
