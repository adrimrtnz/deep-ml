def calculate_parameters(layers: list[dict]) -> int:
    """
    Calculate the total number of trainable parameters in a neural network.

    Args:
        layers: List of dictionaries, each describing a layer.

    Returns:
        Total number of trainable parameters (int).
    """
    params = 0
    labels = {
        'dense': ('input_size', 'output_size'),
        'conv2d': ('in_channels', 'out_channels')
    }

    for l in layers:
        l_type = l.get('type')
        in_label, out_label = labels.get(l_type)
        bias = l.get('bias', True)
        k = l.get('kernel_size', 1)
        params += l[in_label] * l[out_label]*k*k + l[out_label]*bias


    return params