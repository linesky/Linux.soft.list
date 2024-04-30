declare SUB MAIN ()
declare sub clears ()
declare SUB puts (src AS byte ptr)
sub MAIN ()
    const var1 = "OS BUILDER HELLO...."
    clears()
    puts cptr(byte ptr, @var1)
end sub 

sub puts (var1 AS Byte Ptr)
 
    dim var2 as byte ptr
    dim n AS long
 
    var2 = cptr(byte ptr, &HB8000)
 
    n = 0
 
    while var1[n] <> 0
        var2[2 * n] = var1[n]
        var2[2 * n + 1] = &h67
        n = n + 1
    wend
end sub

sub clears ()
 
    dim var2 as byte ptr
    dim n AS long
    
    var2 = cptr(byte ptr, &HB8000)
 
    n = 0
 
    while n <> 2000
        var2[2 * n] = 32
        var2[2 * n + 1] = &h67
        n = n + 1
    wend
end sub
