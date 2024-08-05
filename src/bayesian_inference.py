def infer_concept_importance(model: Callable, guide: Any, observations: torch.Tensor) -> Dict[str, float]:
    """
    Infer the importance of each concept using the trained guide.

    Args:
        model (Callable): The probabilistic model
        guide (Any): The trained guide (posterior approximation)
        observations (torch.Tensor): Observed data

    Returns:
        Dict[str, float]: Importance scores for each concept
    """
    try:
        importance_scores = {}
        trace = pyro.poutine.trace(guide).get_trace(observations)
        for name, node in trace.nodes.items():
            if 'concept_weights' in name:
                importance_scores[name] = node['value'].mean().item()
        return importance_scores
    except Exception as e:
        logger.error(f"Error in infer_concept_importance: {str(e)}")
        raise