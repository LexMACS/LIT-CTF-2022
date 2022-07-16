#include <stdio.h>

int NUM_Q = 10;
int FLAG_LEN = 66;
char* questions[10] = {
    "What is 1+1?",
    "How many sides does a square have?",
    "What is 8*30?",
    "What is the remainder when 39 is divided by 4?",
    "What is the 41st fibbonaci number?",
    "How many questions are on this test?",
    "What number am I thinking of?",
    "What is the answer to this question?",
    "Prove that the answer to the previous question is correct.",
    "Give me an integer."
};

unsigned long long answers[10] = {
    2,
    4,
    240,
    3,
    165580141,
    10,
    5838215,
    111222345,
    543222111,
    9
};

unsigned long long submitted[10] = {0};

unsigned long long flag[] = {
    13188889939062095782U,
11208544126842017913U,
10558804685687107154U,
10306785355211366583U,
9515848926608812910U,
8396981032178126942U,
18344432567112940925U,
10894315417644347509U,
12915435567020127866U,
10236686548230925333U,
9910687835173361033U,
10740973227025784121U,
11387355626471251935U,
13188853513079448603U,
13080843016784753522U,
12900753292752493523U,
9874331068365071144U,
12828510797876981091U,
13653660064251963065U,
10454254865357604787U,
10680349923575943016U,
10887980451809068960U,
10878496334090946521U,
13337676468007957708U,
11319934103585199189U,
9095919600283345709U,
8293112813803947842U,
8642508606979376992U,
14846556244186037922U,
11040480180975926647U,
10884956600336777167U,
10162398873132598899U,
10598943469849811678U,
10824496470691569368U,
10311019501138004214U,
8860942605223970241U,
17590069968127663005U,
10176823202534636272U,
10022883605470819314U,
10626667161368582867U,
5694944082755881598U,
11135681626600569544U,
10450655508716503842U,
10090575040981489248U,
9948379871133511093U,
17541531543849620316U,
9014429887980928373U,
11492192462992874815U,
12788518928726318206U,
10345799454699622927U,
10176134258626725841U,
10527373304769656437U,
11383950147271944361U,
12941104438505934727U,
12768841630835799983U,
12760974374929552289U,
10127565967915053946U,
12864655889244115760U,
13765434172903033541U,
10090599522945947751U,
10558735018145314107U,
10847090637256609354U,
10605977135258598282U,
13623172070402568799U,
10320123250552142539U,
13553956231988918349U
};

void generate_flag(){
    for(int i = 0; i < NUM_Q; i++){
        for(int j = 0; j < FLAG_LEN; j++){
            flag[j] ^= ((submitted[i]^0x94d049bb133111eb) * (j^0xbf58476d1ce4e5b9));
        }
    }
    for(int i = 0; i < FLAG_LEN; i++){
        printf("%c", flag[i]);
    }
    printf("\n");
}

void grade_test(){
    int correct = 0;
    for(int i = 0; i < NUM_Q; i++){
        if(submitted[i] == answers[i]){
            correct++;
        }
    }
    printf("You got %d out of 10 right!\n", correct);
    if(correct == 10){
        printf("Wow! That's a perfect score!\n");
        printf("Here's the flag:\n");
        generate_flag();
    }else{
        printf("If you get a 10 out of 10, I will give you the flag!\n");
    }
}

void main(){
    printf("Welcome to the math test. If you get a perfect score, I will print the flag!\n");
    printf("All questions will have non-negative integer answers.\n\n");
    for(int i = 0; i < NUM_Q; i++){
        printf("Question #%d: ", i+1);
        printf("%s\n", questions[i]);
        scanf("%llu", &submitted[i]);
    }
    grade_test();
}
