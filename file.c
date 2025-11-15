void main(){
    int i;
    int j;
    for(j = 0; j < 10; j = j + 1){
        debug j;
        i = 0;
        while(i < 5){
            debug i;
            i = i + 1; 
        }
    }
}