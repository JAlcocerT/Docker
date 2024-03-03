#RPi

#Get the current wd as the directory of this file
wd<-dirname(rstudioapi::getActiveDocumentContext()$path)
setwd(wd)
#knitt the file on its current folder to test its view
rmarkdown::render('Docker_index.Rmd',
                  output_file = paste('index', 
                                      '.html', sep=''))