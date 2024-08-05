# scripts/run_experiment.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from probabilistic_model import mathematical_concept_model
from structure_learning import structure_learning
from bayesian_inference import bayesian_inference
from formal_verification import verify_concept
from symbolic_reasoning import SymbolicReasoning
from utils import load_data, generate_theorems, output_results

def main():
    input_data = load_data()

    concepts, observations = mathematical_concept_model(input_data)

    learned_structure = structure_learning(observations, mathematical_concept_model)

    posterior = bayesian_inference(mathematical_concept_model, observations)

    for concept in concepts:
        verification_result = verify_concept(concept)
        print("Verification result for concept:", verification_result)

    symbolic_reasoning = SymbolicReasoning()
    for theorem in generate_theorems(concepts):
        proof = symbolic_reasoning.prove_theorem(theorem, concepts)
        print("Proof for theorem:", proof)

    output_results(concepts, learned_structure, posterior)

if __name__ == "__main__":
    main()