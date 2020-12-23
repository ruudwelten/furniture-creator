# Technical challenge - Software Engineer

## Challenge description
For a production facility that assembles furniture. We simplified how the real
facility works, for the purpose of this technical challenge:  

- It uses parts of different types and sizes as input;  
- It produces products of different designs and sizes as output;  
- The people in the production facility are assembling products by design
  specifications that tell how many parts are needed of which kinds;  
- The parts arrive into the facility one by one, and they can be stored there
  until there's enough parts to assemble a product.  

Your job is to create an application that takes the product designs and the
stream of parts as an input, and produce the stream of products as an output.  

The application needs to work as a command line application using standard input
and standard output.  

It can be written in any of the following languages: Python, Ruby, Go,
JavaScript, TypeScript, PHP.  

Completing the challenge should take approximately 4 hours and we expect you to
return it in the next couple of days. If you see you're exceeding the 4 hours,
you should submit your solution as it is, with a short explanation of what is
left and how you would finish the challenge.  

## Input / output format specifications
- A **part type** is identified by a single, lowercase letter: `a - z`;  
- A **part size** is indicated by a single, uppercase letter: `L` (large) and
  `S` (small).
- A **part** is identified by a **part type** and a **part size**: for
  example, `rL`.  
- A **product name** is indicated by a string in square brackets: `[Chair]`;  
- A **product size** is indicated by a single, uppercase letter: `L` (large) and
   `S` (small).
- A **product design** is a single line of characters with the following format:  
  ```xml
  <product name><product size><part 1 quantity><part 1 type>...<part N
  quantity><part N type><total quantity of
  parts in the product>
  ```  
  **Example**: [Chair]L5d8s11t32  
- A **product** is a single line of characters with the following format:  
  ```xml
  <product name><product size><part 1 quantity><part 1 type>...<part N
  quantity><part N type>
  ```  
  **Example**: [Chair]L5d8s11t8y  
- The **product design** and **product** formats include a **product size** but
  no **part sizes**. This is because large *products* are only made from large
  *parts*, and small *products* are only made from small *parts*.  
- The **part types** are listed in alphabetic order and only appear once in
  both **product designs** and **products**.  
- The **part quantities** are always larger than 0 for both **product designs**
  and **products**.  
- The **total quantity of parts in the product** for **product design** can be
  bigger than the sum of the **parts quantities**, allowing extra space in the
  products that can consist of any kind of part.  
- The **product** does not have a **total quantity of parts in the product**
  specified, but the sum of the **part quantities** should be equal to the
  **total quantity of parts in the product** of the corresponding **product
  design**.  
- The **input stream** structure will follow this structure:
  ```
  product design1
  product design2
  <empty line>
  part1
  part2
  part3
  ...
  ```
  **Example**:
  ```
  [Chair]S2a5c7j20
  [Chair]L9d7g8u30

  aS
  dL
  gL
  uL
  jS
  ...
  ```
- The **output** should be a **product** every time one can be created from the
  available **parts** according to one of the provided **product designs**:
  ```
  product1
  product2
  ...
  ```
  **Example**:
  ```
  [Chair]L9d8g8u5v
  [Chair]S4a7c9j
  ...
  ```
