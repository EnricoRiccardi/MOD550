def mean_squared_error(observed, predicted):
    """ Compute the mean squared error.

    Paramets:
    ---------
    observed : list,
        The observed values.
    predicted : list,
        The predicted values.

    Output:
    ------
    sys[0] : float,
       Mean squared error.

    """
    if len(observed) != len(predicted):
        raise ValueError(
            "The lengths of input lists are" +
            f"not equal {len(observed)} {len(predicted)}.")
    
    # Initialize the sum of squared errors
    sum_squared_error = 0
    
    # Loop through all observations
    for obs, pred in zip(observed, predicted):
        # Calculate the square difference, and add it to the sum
        sum_squared_error += (obs - pred) ** 2
    
    # Calculate the mean squared error
    mse = sum_squared_error / len(observed)
    
    return mse
