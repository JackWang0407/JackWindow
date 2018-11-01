

@IF not "%1" == "" (
	@IF not "%2" == "" (
		ffmpeg.exe -y -i %1 -filter:v yadif -acodec aac -ar 44100 -ab 128k -ac 2 -vcodec libx264 -preset slow -crf 20 -async 512 -strict -2 -threads 1 %2
	) ELSE (
		echo [ERROR] CMD : %0 input_filename output_filename
	)
) ELSE (
        echo [ERROR] CMD : %0 input_filename output_filename
)
