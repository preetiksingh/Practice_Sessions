
item_catalog={"CDs":12.90,"USB Drivers":13.40,"Keyboards":13}
for x in item_catalog:
    print x
    
def exists_in(A,name):
    result=False
    for x in A:
        if x==name:
            result=True
    return result
exit_var=False
while exit_var==False:
    in_var=raw_input("Enter a product to look up price (or press x to exit)")
    if exists_in(item_catalog,in_var):
        print "the price of the item is:"
        print item_catalog[in_var]
    if exists_in(item_catalog,in_var) == False and in_var !="x":
        print"the item does not exists"
    if in_var =="x":
        exit_var=True
    
    