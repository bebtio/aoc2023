#include "readlines.hpp"



std::vector< std::string >
readLines( std::string inputFile )

{
    std::vector< std::string > lines;
    std::ifstream fileStream( inputFile );

    std::string line;
    while( std::getline( fileStream, line) )
    {
        line = std::regex_replace(line, std::regex("\n+"),"");
        lines.push_back( line );
    }


    return( lines );

}