from pytube import YouTube

YouTube("https://www.youtube.com/watch?v=H7S2tFbgcM8&list=RDH7S2tFbgcM8&start_radio=1").streams.first().download()
