lines = File.open("input.txt").readlines.map(&:chomp)
lines.delete("")

BD = "out-of-order"
EQ = "equal"
GD = "in-order"

def check_ret(res)
    return (res == BD or res == GD)
end

def int_cmp(l, r)
    # p "INT_CMP #{l}, #{r}"
    if l < r
        return GD
    elsif r < l
        return BD
    end

    return EQ
end

def ll_cmp(l, r)
    # p "LL_CMP #{l}, #{r}"
    while true
        if l.length == 0 and r.length == 0
            return EQ
        end

        if l.length == 0
            return GD
        end

        if r.length == 0
            return BD
        end

        l_popped = l[0]
        r_popped = r[0]
        l = l.drop(1)
        r = r.drop(1)

        res = cmp(l_popped, r_popped)
        if check_ret(res)
            return res
        else
            return cmp(l, r)
        end
    end

    return EQ
end

def cmp(l, r)
    # p "CMP #{l}, #{r}"
    l_arr = l.is_a? Array
    l_int = l.is_a? Integer
    r_arr = r.is_a? Array
    r_int = r.is_a? Integer

    if l_arr and r_arr
        res = ll_cmp(l, r)
        return res if check_ret(res)
    elsif l_int and r_arr
        res = cmp([l], r)
        return res if check_ret(res)
    elsif l_arr and r_int
        res = cmp(l, [r])
        return res if check_ret(res)
    elsif l_int and r_int
        res = int_cmp(l, r)
        return res if check_ret(res)
    end

    return EQ
end

sum = 0
lines.map{|x| eval(x)}.each_slice(2).with_index do |(l, r), index|
    res = cmp(l, r)
    if res == GD or res == EQ
        sum += index + 1
    end
end

p sum