
def subtract_min_quantile(intensities, min_quantile=.01):
    """
    Subtract the intensity defined by the minimum quantile from all columns 
    
    @param intensities dataframe
        The dataframe of intensities
        
    min_quantile: float
        The minimum quantile to be consider zero
    
    returns: 
        dataframe with rescaled intensities
    """
    
    columns_min_quantile = intensities.quantile(min_quantile)
    #print(columns_min_quantile)

    subtracted_min = intensities - columns_min_quantile 
    #print(subtracted_min)

    #clip negative values to zero
    subtracted_min.clip(lower=0, axis=1, inplace=True)

    return subtracted_min 


    

    