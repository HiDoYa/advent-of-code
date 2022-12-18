lines = File.open("input.txt").readlines.map(&:chomp).map(&:strip)
lines.delete("")

class Monkey
    def initialize(items, operator, operand, divisible_cond, true_monkey_index, false_monkey_index)
        @inspected_count = 0
        @items = items 

        # Operation
        @operator = operator
        @operand = operand

        # Jump cond
        @divisible_cond = divisible_cond
        @true_monkey_index = true_monkey_index
        @false_monkey_index = false_monkey_index
    end

    attr_accessor :items
    attr_reader :inspected_count, :divisible_cond

    def inspect_item(item, divisible_lcm)
        @inspected_count += 1

        if @operand == "old"
            operand_val = item
        else
            operand_val = @operand.to_i
        end

        if @operator == "+"
            new_item = item + operand_val
        end

        if @operator == "*"
            new_item = item * operand_val
        end

        new_item = new_item % divisible_lcm

        jump_index = (new_item % @divisible_cond == 0) ? @true_monkey_index : @false_monkey_index

        return new_item, jump_index
    end

    def do_turn(monkeys, divisible_lcm)
        while not @items.empty?
            # Get first item
            item = @items[0]
            @items.shift

            new_item, jump_index = self.inspect_item(item, divisible_lcm)
            monkeys[jump_index].items.append(new_item)
        end
    end
end

monkeys = []

lines.each_slice(6) do |line|
    items = line[1].split(":")[1].split(",").map(&:strip).map(&:to_i)

    # Operation will usually involve a const, one special case is old*old
    operation = line[2].split("=")[1].strip.delete_prefix("old").strip
    operator = operation[0]
    operand = operation[1..-1].strip

    # Jump cond
    divisible_cond = line[3].split(" ")[-1].to_i
    true_monkey_index = line[4].split(" ")[-1].to_i
    false_monkey_index = line[5].split(" ")[-1].to_i

    monkey = Monkey.new(
        items=items,
        operator=operation[0],
        operand=operand,
        divisible_cond=divisible_cond,
        true_monkey_index=true_monkey_index,
        false_monkey_index=false_monkey_index,
    )

    monkeys.append(monkey)
end

divisible_lcm = monkeys.map{|monkey| monkey.divisible_cond}.reduce(1, :lcm)

10000.times do |x|
    monkeys.each do |monkey|
        monkey.do_turn(monkeys, divisible_lcm)
    end
end


nums = monkeys.map{|x| x.inspected_count}.sort[-2..-1]
p nums[0] * nums[1]
