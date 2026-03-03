
# lb_lazy_input
© Copyright logic-break 2026

https://github.com/logic-break/logic-break/tree/main/libraries/lb_lazy_input

> lib made for lazy, by lazy  

installation:

    pip install lb-lazy-num

**NOTE: in code, you must import lb_lazy_num**


# Usage

 - .format_num(value, precision=2) : converts from 1000000 to 1M, supports up to Qi, if more than Qi, returns unchanged value
 - .convert_size(value_str, target_unit) : returns converted size, for example .convert_size("1024MB", "GB") wil return 1GB, this supports up to PB, if more idk :)
 
 # Example:

    import lb_lazy_input
     
    z = input("Enter value:\n")
    x = input("Convert this value from: (B, KB, MB, GB, TB, PB)\n")
    c = input("Convert this value to: \n")
    
    v = z + x
    result = lb_lazy_input.convert_size(v, c)
    print(result)
