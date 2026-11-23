"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    Encoding utilities for handling multi-language PSG headers and metadata.
    
    PSG files often contain headers encoded in Latin-1 (ISO-8859-1), Windows-1252,
    or other single-byte encodings, especially when recorded in non-English labs.
    
    These utilities ensure consistent UTF-8 encoding for all output files.
"""


def ensure_utf8_string(value):
    """
    Convert string values to UTF-8, auto-detecting source encoding when needed.
    
    Handles multiple encodings commonly found in PSG headers:
    - Latin-1 / ISO-8859-1 (French, German, Spanish, Portuguese, Dutch)
    - Windows-1252 (Western European Windows systems)
    - UTF-8 (already valid)
    - Other single-byte encodings (fallback detection)
    
    For robustness, tries encoding detection only if string contains non-UTF-8 bytes.
    This avoids expensive charset detection for pure ASCII and valid UTF-8 strings.
    
    Args:
        value: String or other value potentially in non-UTF-8 encoding
        
    Returns:
        UTF-8 decoded string, or original value if not a string.
        Invalid bytes are replaced with U+FFFD (replacement character).
        
    Examples:
        >>> ensure_utf8_string("Patient: José García")  # Already UTF-8
        'Patient: José García'
        
        >>> ensure_utf8_string("Patient: Jérôme")  # Latin-1 French
        'Patient: Jérôme'
    """
    if not isinstance(value, str):
        return value
    
    try:
        # Fast path: if string is already valid UTF-8, return it unchanged
        value.encode('utf-8').decode('utf-8')
        return value
    except (UnicodeEncodeError, UnicodeDecodeError):
        pass
    
    # The string contains non-UTF-8 characters. Try common encodings used in PSG files.
    # Order: most common first to minimize re-encoding attempts.
    for encoding in ['latin-1', 'windows-1252', 'iso-8859-15', 'cp1250', 'utf-16']:
        try:
            # Encode as source encoding, decode as UTF-8
            return value.encode(encoding).decode('utf-8')
        except (UnicodeDecodeError, UnicodeEncodeError, LookupError):
            continue
    
    # Final fallback: encode with error replacement to ensure no exception
    # This converts undecodable bytes to U+FFFD (replacement character)
    try:
        return value.encode('utf-8', errors='replace').decode('utf-8', errors='replace')
    except Exception:
        # Should rarely reach here, but if so: strip non-decodable characters
        return value.encode('ascii', errors='ignore').decode('ascii')


def sanitize_subject_info_for_export(subject_info_dict):
    """
    Prepare subject_info dictionary for UTF-8 export by converting all string values.
    
    Args:
        subject_info_dict: Dictionary with subject metadata (filename, id1, id2, etc.)
        
    Returns:
        Dictionary with all string values converted to proper UTF-8
    """
    if not isinstance(subject_info_dict, dict):
        return subject_info_dict
    
    sanitized = {}
    for key, value in subject_info_dict.items():
        if isinstance(value, str):
            sanitized[key] = ensure_utf8_string(value)
        else:
            sanitized[key] = value
    
    return sanitized
