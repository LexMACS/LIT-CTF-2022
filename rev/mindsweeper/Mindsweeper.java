import java.util.Random;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;
import java.io.File;
import java.io.FileNotFoundException;

public class Mindsweeper{
    static final int LENGTH = 32;
    static void d(boolean[][] b, boolean[][] f){
        for(int i = 0; i < 32; i++){
            for(int j = 0; j < LENGTH; j++){
                if(f[j][i]){
                    if(b[j][i]) System.out.print("*");
                    else System.out.print(" ");
                }else{
                    System.out.print("?");
                }
            }
            System.out.println();
        }
    }
    public static void main(String[] args) throws InterruptedException{
        Random r = new Random();
        boolean[][] b = new boolean[LENGTH][32], f = new boolean[LENGTH][32];
        int clears = 0, mines = 0;
        for(int i = 0; i < LENGTH; i++){
            int l = r.nextInt();
            for(int j = 0; j < 32; j++){
                b[i][j] = ((l >>> j) & 1) == 1;
                if(b[i][j]) mines++;
                else clears++;
            }
        }
        for(int i = 0; i < 256; i++){
            int x = r.nextInt(LENGTH);
            int y = r.nextInt(32);
            if(f[x][y]){
                i--;
                continue;
            }
            f[x][y] = true;
            if(b[x][y]){
                mines--;
            }else{
                clears--;
            }
        }
        String welcome = "Welcome to Mindsweeper - Minesweeper but a bit harder";
        System.out.println(welcome);
        System.out.print("Loading");
        for(int i = 0; i < 10; i++){
            System.out.print(".");
            for(long stop=System.nanoTime() + TimeUnit.MILLISECONDS.toNanos(r.nextInt(100)+100); stop > System.nanoTime();){
                r = new Random();
            }
        }
        System.out.println();
        Scanner in = new Scanner(System.in);
        boolean win = false, pb = false;;
        while(true){
            if(!pb){
                d(b, f);
            }
            System.out.println("Enter your guess: ");
            String cmd = in.next();
            int x = -1, y = -1;
            try{
                x = in.nextInt();
                y = in.nextInt();
            }catch(Exception e){}
            if(x < 0 || y < 0 || x >= LENGTH || y >= 32){
                System.out.println("Invalid position");
                pb = true;
                continue;
            }
            if(f[x][y]){
                System.out.println("Already guessed this spot!");
                pb = true;
                continue;
            }
            if(cmd.equals("clear")){
                if(b[x][y]){
                    break;
                }
                f[x][y] = true;
                clears--;
            }else if(cmd.equals("mine")){
                if(!b[x][y]){
                    b[x][y] = true;
                }
                f[x][y] = true;
                mines--;
            }else{
                System.out.println("Invalid command");
                pb = true;
                continue;
            }
            pb = false;
            if(clears == 0 && mines == 0){
                win = true;
                break;
            }
        }
        if(win){
            System.out.println("I don't know how you did it, but you won!");
            try{
                Scanner flagInput = new Scanner(new File("flag.txt"));
                System.out.println(flagInput.nextLine());
            }catch(FileNotFoundException e){
                System.out.println("No flag.txt file found. If this is on the server, please contact an admin.");
            }
        }else{
            System.out.println("BOOM! A mine exploded. You didn't win :(");
        }
    }
}
