//This is an optimised code to covert a binary number to any base. The one line operation handles all types of bases(including hexadecimal numbers)

public class Main {
    static String convert(String num, int fromBase, int toBase) {
        return Integer.toString(Integer.parseInt(num, fromBase), toBase).toUpperCase();
    }
    
    public static void main(String[] args) {
        String binary = "11101";
        System.out.println(convert(binary, 2, 6)); //Base 2 to Base 6
        System.out.println(convert(binary, 2, 10)); // Base 2 to Base 10
        System.out.println(convert(binary, 2, 16)); //Base 2 to Base 16(hex)
        System.out.println(convert("FF", 16, 2)); //Base 16 to Base 2
    }
}
