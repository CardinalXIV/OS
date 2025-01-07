#include <semaphore.h>
#include <stdio.h> 
#include <pthread.h> 
#include <unistd.h>
#include <time.h>        

#define NUM_ITERATIONS 1000 //iterations to run

sem_t sem; //semaphore variable

//signal semaphore every 50ms
void *task1(void *arg) {
    for (int i = 0; i < NUM_ITERATIONS; i++) { 
        sem_post(&sem);
        usleep(50000);  
    }
    return NULL; 
}

//wait for semaphore
void *task2(void *arg) {
    struct timespec start, end; 
    FILE *f = fopen("semaphore_latencies.txt", "w"); // cjange the file name if needed based on what you save
    if (f == NULL) {
        perror("error opening file");

        return NULL;
    }
    for (int i = 0; i < NUM_ITERATIONS; i++) {  
        clock_gettime(CLOCK_MONOTONIC, &start); //start timer
        sem_wait (&sem); 
        clock_gettime( CLOCK_MONOTONIC , &end);  //get  the timer value 

        long time_taken = (end.tv_sec - start.tv_sec) * 1000000 + (end.tv_nsec - start.tv_nsec) / 1000;
        fprintf(f, "%ld\n", time_taken); //save file
    }
    fclose(f);
    return NULL; 
}
//follow research paper pseudocode 
int main() {
    pthread_t t1, t2;  
    sem_init(&sem, 0, 0);  //set semaphore to =0
    pthread_create(&t1, NULL, task1, NULL);  
    pthread_create(&t2, NULL, task2, NULL);  
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    sem_destroy(&sem);  
    return 0;  
}
