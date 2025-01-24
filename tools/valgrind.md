Check compiled c++ programme ./bin/test_my  
valgrind --tool=memcheck --leak-check=full --show-leak-kinds=all --log-file=memchk1.log ./bin/test_my