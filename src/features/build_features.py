import pandas as pd

def _map_binary_series(s: pd.Series) -> pd.Series:
    vals = list(pd.Series(s.dropna().unique()).astype(str))
    valset = set(vals)

    if valset == {"Yes", "No"}:
        return s.map({"Yes": 1, "No": 0}).astype("Int64")
    
    if valset == {"Male", "Female"}:
        return s.map({"Male": 1, "Female": 0}).astype("Int64")

    if len(valset) == 2:
        sorted_values = sorted(vals)
        mapping = {sorted_values[0]: 0, sorted_values[1]: 1}
        return s.astype(str).map(mapping).astype("Int64")
    
    return s

def build_features(df: pd.DataFrame, target_col: str = "Churn") -> pd.Series:
    df = df.copy()

    obj_cols = [col for col in df.select_dtypes(include = ["object"]).columns if col != target_col]
    num_cols = [col for col in df.select_dtypes(include = ["int64", "float64"]).columns if col != target_col]

    print(f"Found {len(obj_cols)} object columns and {len(num_cols)} numeric columns.")

    binary_cols = [c for c in obj_cols if df[c].dropna().nunique() == 2]
    multi_cols = [c for c in obj_cols if df[c].dropna().nunique() > 2]

    print(f"Found {len(binary_cols)} binary columns and {len(multi_cols)} multi-category features.")
    if binary_cols:
        print(f"Binary features: {binary_cols}")
    if multi_cols:
        print(f"Multi-category features: {multi_cols}")
    
    if binary_cols:
        for col in binary_cols:
            df[col] = _map_binary_series(df[col])
            print(f"{col} converted to binary encoding.")

    bool_cols = df.select_dtypes(include = ["bool"]).columns.tolist()
    if bool_cols:
        df[bool_cols] = df[bool_cols].astype(int)
        print(f"Converted {len(bool_cols)} boolean columns to int: {bool_cols}")
    

    if multi_cols:
        original_shape = df.shape
        df = pd.get_dummies(df, columns=multi_cols, drop_first=True)
        print(f"Created {df.shape[1] - original_shape[1] + len(multi_cols)} features from {len(multi_cols)} columns.")
    
    for c in binary_cols:
        if pd.api.types.is_integer_dtype(df[c]):
            df[c] = df[c].fillna(0).astype(int)
        
    print(f"Feature engineering complete: {df.shape[1]} final features")
    return df