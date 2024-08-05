def evaluate_concept(concept: Callable, data: torch.Tensor) -> float:
    """
    Evaluate a mathematical concept based on its ability to fit the data.

    Args:
        concept (Callable): The concept to evaluate
        data (torch.Tensor): The data to fit

    Returns:
        float: The evaluation score (lower is better)
    """
    try:
        predicted = concept(data)
        mse = torch.mean((predicted - data) ** 2)
        complexity = concept_complexity(concept)
        return mse.item() + 0.1 * complexity
    except Exception as e:
        logger.error(f"Error in evaluate_concept: {str(e)}")
        raise

def concept_complexity(concept: Callable) -> int:
    """
    Estimate the complexity of a concept based on its string representation.

    Args:
        concept (Callable): The concept to evaluate

    Returns:
        int: The estimated complexity
    """
    try:
        return len(str(concept))
    except Exception as e:
        logger.error(f"Error in concept_complexity: {str(e)}")
        raise

def rank_concepts(concepts: List[Callable], data: torch.Tensor) -> List[Tuple[Callable, float]]:
    """
    Rank concepts based on their evaluation scores.

    Args:
        concepts (List[Callable]): The concepts to rank
        data (torch.Tensor): The data to use for evaluation

    Returns:
        List[Tuple[Callable, float]]: Ranked concepts with their scores
    """
    try:
        ranked = [(concept, evaluate_concept(concept, data)) for concept in concepts]
        return sorted(ranked, key=lambda x: x[1])
    except Exception as e:
        logger.error(f"Error in rank_concepts: {str(e)}")
        raise