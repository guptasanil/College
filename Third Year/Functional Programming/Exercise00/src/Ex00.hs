module Ex00 where

name, idno, username :: String
name      =  "Gupta, Sanil"  -- replace with your name
idno      =  "18322581"    -- replace with your student id
username  =  "guptas1"   -- replace with your TCD username


declaration -- do not modify this
 = unlines
     [ ""
     , "@@@ This exercise is all my own work."
     , "@@@ Signed: " ++ name
     , "@@@ "++idno++" "++username
     ]

{- Modify everything below here as you see fit to ensure all tests pass -}

hello  =  "Hello World :-)"
