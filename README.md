# VI-CORE

## Personal assistant system

### utilities 
>spark moudel which has the Listen(speech recognition) & Talk(gTTS) functions


### CORE-CEREBRUM
> The Think class is where the magic happens it loops through the intents.json(no exection) to see if the input
> matches the pattrens there if not then it jumps to sandbox (features)

### Sandbox
> the sandbox is a module contain VI's features each feature has two functions :

#### description 
> contant is a dict which has Pattrens and responses 

#### execute 
> is if the input matches one of the patterns the execute func will run

<img src="https://github.com/astroxiii/VI-CORE/blob/main/presentation.png" width="500"/>
